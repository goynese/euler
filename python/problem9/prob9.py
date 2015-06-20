import sys
import math

def pythagorean_triplet():
    for a in range(1, 500):
        for b in range(1, 500):
            c = math.sqrt(a*a + b*b)
            if (a + b + c) == 1000:
                return a*b*c

if __name__ == "__main__":
    print pythagorean_triplet()
