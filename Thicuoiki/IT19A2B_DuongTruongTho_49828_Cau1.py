import math


def isPrimeNumber(n):
    if n < 2:
        return False
    # check so nguyen to khi n >= 2
    squareRoot = int(math.sqrt(n))
    for i in range(2, squareRoot + 1):
        if n % i == 0:
            return False
    return True

def printPrime(start, end):
    for i in range(start, end + 1):
        if isPrimeNumber(i):
            print(i, end=' ')
    print()


def main():
    printPrime(30, 200)


if __name__ == '__main__':
    main()