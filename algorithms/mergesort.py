import math, secrets

def merge_sort(list_):
    list_length = len(list_)

    # Exit condition
    if list_length <= 1:
        return list_

    m = math.floor(list_length/2)
    merged = []
    left = merge_sort(list_[0:m])
    right = merge_sort(list_[m:list_length])

    i = 0
    k = 0
    while i < len(left) and k < len(right):
        if left[i] < right[k]:
            merged.append(left[i])
            i+=1
        elif left[i] > right[k]:
            merged.append(right[k])
            k+=1
        else:
            merged.append(left[i])
            merged.append(right[k])
            i+=1
            k+=1

    # append whats left
    merged = merged + left[i:len(left)]
    merged = merged + right[k:len(right)]

    return merged


def main():
    input = [secrets.randbelow(50) for i in range(10)]
    print(f"Input: {input}")
    output = merge_sort(input)
    print(f"Output: {output}")


if __name__ == '__main__':
    main()