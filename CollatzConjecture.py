import sys


def collatzConjectureIter(n):
    while n != 1:
        if (n % 2 == 0):
            n = n / 2
            print(n)
        else:
            n = n * 3 + 1
            print(n)


def collatzConjectureRecIter(n):
    if n == 1:
        sys.exit()
    else:
        if (n % 2 == 0):
            n = n / 2
            print(n)
            collatzConjectureRecIter(n)
        else:
            n = n * 3 + 1
            print(n)
            collatzConjectureRecIter(n)


#collatzConjectureRecIter(9)
#collatzConjectureIter(9)

