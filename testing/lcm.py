#
# Calculate the lowest common multiplicator (lcm)
#
from time import time

def lcm(a, b):
    # init cache
    cache_a = []
    cache_b = []

    i = 1
    while True:
        x = a*i
        cache_a.append(x)
        if x in cache_b:
            break

        x = b*i
        cache_b.append(x)
        if x in cache_a:
            break
        i+=1
    print(x)

def lcm_optimized(a, b):
    # Assign to define vars
    # so it is clear x is always the bigger number
    if a > b:
        x = a
        y = b
    else:
        x = b
        y = a

    xi = 1
    yi = 1
    while True:

        if (x*xi) % (y*yi) == 0:
            break

        if (y*yi) > (x*xi):
            xi+=1
        yi+=1
    print(x*xi)

if __name__ == '__main__':
    tstart = time()
    lcm(52, 60)
    lcm(58, 64)
    lcm(58, 614)
    lcm(55678, 614)
    print(time()-tstart)
    # TODO: Optimization could be done by only checking the smaller
    # number when it becomes a divisor of a multiplication of the bigger
    # number
    tstart = time()
    lcm_optimized(52, 60)
    lcm_optimized(58, 64)
    lcm_optimized(58, 614)
    lcm_optimized(55678, 614)
    print(time()-tstart)

    # Output:
    #   780
    #   1856
    #   17806
    #   17093146
    #       Time 6948.689222335815 milliseconds
    #   780
    #   1856
    #   17806
    #   17093146
    #       Time 6.639957427978516 milliseconds
    #   --> huge improvement!