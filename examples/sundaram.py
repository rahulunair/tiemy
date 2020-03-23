"""sundaram's sieve to find non primes.
src: https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/2073279#2073279
"""
from tiemy import timer


@timer
def sundaram(N):
    """sundaram's sieve to find non primes"""
    numbers = list(range(3, N, 2))
    half = (N) // 2
    init = 4

    for step in range(3, N, 2):
        for i in range(init, half, step):
            numbers[i - 1] = 0
        init += 2 * (step + 1)
        if init > half:
            return [2] + list(filter(None, numbers))


if __name__ == "__main__":
    sundaram(1000000)
