import sys

def sum():
    sum = 0
    for n in range(1000):
        if n%3 == 0 | n%5 == 0:
            sum += n
    return sum


if __name__ == "__main__":
    print sum()