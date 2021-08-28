#
# This will be an example how to encrypt and decrypt
# message in a img (format png)
#

import pathlib
import cv2
import math


IMG_FILENAME = 'sample.png'
HIDDEN_MSG = 'This is a steganography test!This is a steganography!This is a steganography!This is a steganography!This is a steganography!This is a steganography!This is a steganography!This is a steganography!This is a steganography!This is a steganography'


class Application:

    def __init__(self):
        self.base_dir = pathlib.Path(__file__).parent.absolute()

    def load_image(self, filepath):
        img = cv2.imread(filepath)
        return img

    def encrypt(self, msg, filename):

        img = self.load_image(self.base_dir.joinpath(filename).as_posix())
        data = [format(ord(_c), '08b') for _c in msg]
        _, width, _ = img.shape
        required_pixel = len(data) * 3 * 8
        required_rows = math.ceil(required_pixel/width)
        max_per_row = width-(width%3)
        # image position
        i_pos = 0
        # data position
        d_pos = 0
        for i in range(required_rows + 1):
            # Step 4
            while(i_pos < (max_per_row) and d_pos < len(data)):
                char = data[d_pos]
                d_pos += 1
                # Step 5
                # iterating through bits
                for index_k, k in enumerate(char):
                    
                    # current position of the data bit
                    db_pos = index_k % 3 # 0,1,2

                    # Change last bit
                    if(k == '1' and img[i][i_pos][db_pos] % 2 == 0):
                        img[i][i_pos][db_pos]+=1
                    elif(k == '0' and img[i][i_pos][db_pos] % 2 == 1):
                        img[i][i_pos][db_pos]-=1
                    
                    # Jump to next pixel
                    if(db_pos == 2):
                        i_pos+= 1

                    # End of current data
                    if(index_k == 7):
                        if(d_pos*3*8 < required_pixel and img[i][i_pos][2] % 2 == 1):
                            img[i][i_pos][2] -= 1
                        if(d_pos*3*8 >= required_pixel and img[i][i_pos][2] % 2 == 0):
                            img[i][i_pos][2] -= 1
                        # Jump to next pixel
                        i_pos += 1

                    if i_pos >= max_per_row:
                        i+=1
                        i_pos = 0

            i_pos = 0

        cv2.imwrite(self.base_dir.joinpath("sample_encrypted.png").as_posix(), img)

        return "sample_encrypted.png"

    def decrypt(self, filename):
        img = self.load_image(self.base_dir.joinpath(filename).as_posix())
        _, width, _ = img.shape
        max_per_row = width-(width%3)
        data = ['']
        d_pos = 0
        b_pos = 0
        stop = False
        for i in img:
            if stop:
                break
            for index_p, p in enumerate(i):
                if index_p >= max_per_row:
                    continue
                for index_b, b in enumerate(p):
                    if index_p % 3 == 2 and index_b == 2 and bin(b)[-1] == '1':
                        stop = True
                        break
                    if index_p % 3 != 2 or (index_p % 3 == 2 and index_b != 2):
                        data[d_pos]+= str(bin(b)[-1])
                        b_pos+= 1
                    if b_pos % 8 == 0 and index_b != 2:
                        d_pos+= 1
                        data.append('')
                if stop:
                    break
        data.pop()
        return ''.join([chr(int(c_, 2)) for c_ in data])


    def simulate(self, hidden_msg, img_filename):
        print("Executing the steganography test....")
        print(f"Secret \"{hidden_msg}\" will be hidden in the img")
        print("Running encryption...")
        new_filename = self.encrypt(hidden_msg, img_filename)
        print(f"Name of the new file {new_filename}")
        print("Running decryption...")
        hidden_msg = self.decrypt(new_filename)
        print(f"Secret \"{hidden_msg}\" found in the img")


# Main function
def main():
    app = Application()
    app.simulate(HIDDEN_MSG, IMG_FILENAME)


if __name__ == "__main__":
    main()