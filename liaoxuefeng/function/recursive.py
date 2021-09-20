# coding:utf-8

def fact(n):
    if n == 1:
        return 1

    return n * fact(n-1)


def fact_tail_iter(n, prod=1):
    if n == 1:
        return prod
    return fact_tail_iter(n-1, prod * n)


if __name__ == '__main__':
    print(fact(5))
    print(fact_tail_iter(5))
