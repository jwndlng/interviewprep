#
# Basics to use lists, comprehension and generator
#

def simple_list():
    return [1,2,3,4,5,6,7]

def list_comprehension():
    return [i for i in range(8)]

def list_generator():
    return (i for i in range(8))

def list_generator_2():
    i = 0
    while i < 8:
        yield i
        i+=1

def main():
    
    print(f"Simple list {simple_list()}")
    print(f"List Comprehension {list_comprehension()}")
    print(f"List generator 1 {simple_list()}")
    print(f"List generator 2 {simple_list()}")

if __name__ == "__main__":
    main()