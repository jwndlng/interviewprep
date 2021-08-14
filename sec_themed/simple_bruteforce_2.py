
# Simple Password Bruteforcer with supportance for ascii 33->126
# using a python generator

import time
from itertools import product


# ASCII character start -> end
char_mapping = (33, 126)

def bruteforce_solutions(max_length=5) -> str:
    i = 1
    while True:
        solutions = product(
            [chr(c) for c in range(char_mapping[0], char_mapping[1])],
            repeat=int(i)
        )
        yield solutions
        i+=1
        if i > max_length:
            break

def get_pwd(combination):
    return ''.join(combination)

class Application:

    def testbed(self):
        return ('John Doe', '^&%&')        

    def login(self, passwd, passwd2):
        return passwd == passwd2

    def simulate(self):
        ms_start = time.time()
        found_pw = False
        print("Starting".ljust(80, '.'), str(ms_start-ms_start))
        username, password = self.testbed()
        solutions = bruteforce_solutions()
        for sols in solutions:
            if found_pw:
                break
            for sol in sols:
                if self.login(password, get_pwd(sol)):
                    print(get_pwd(sol))
                    found_pw = True
                    break
        ms_end = time.time()

        if found_pw:
            result = f"Found password {password} = {get_pwd(sol)}"
        else:
            result = "No password found"

        print(result.ljust(80, '.'), str((ms_end-ms_start)*1000))


if '__main__' == __name__:
    app = Application()
    app.simulate()
