import sys, time, numpy, random
from numba import njit

u = int(sys.argv[1])

@njit
def main():

    const = 10000
    r = numpy.random.randint(0, const)
    a = numpy.zeros(const)
    x = sum([ol % u for ol in range(100000)])

    for i in range(const): a[i] += (x + r)
    print(a[r])


start = time.time()
main()
print(time.time() - start)
