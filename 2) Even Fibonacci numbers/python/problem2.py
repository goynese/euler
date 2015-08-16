import sys

def sum_of_multiples():
    sum = 0
    for i in range(1000):
        if i%3 == 0 or i%5 == 0:
            sum+=i 
    return sum

if __name__ == "__main__":
    
    print sum_of_multiples()
    # print Fibonacci(int(sys.argv[1]))