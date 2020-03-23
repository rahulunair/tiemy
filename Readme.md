# Tiemy

A minimalistic timer decorator for timing functions

Tiemy runs decorated functions 3 times and prints mean
and standard deviation of the runs.

Many a time when i wanted to do quick assements, i had to
write some boilerplate to do this, so finally creating a
module for this.

## Easy to Install

```python
pip install tiemy
```

Usage

```python
from tiemy import timer



@timer
def sundaram(N):
	"""sundaram's sieve to find non primes.
	src: https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/2073279#2073279
	"""
    numbers = list(range(3, N, 2))
    half = (N)//2
    init = 4

    for step in range(3, N, 2):
        for i in range(init, half, step):
            numbers[i-1] = 0
        init += 2 * (step + 1)
        if init > half:
            return [2] + list(filter(None, numbers))


if __name__ == "__main__":
    sundaram(100000)
	
```
  


