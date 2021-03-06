"""
Дано число 1≤n≤10^7, необходимо найти последнюю цифру n-го числа Фибоначчи.

Как мы помним, числа Фибоначчи растут очень быстро, поэтому при их вычислении нужно быть аккуратным с переполнением.
В данной задаче, впрочем, этой проблемы можно избежать, поскольку нас интересует только последняя цифра числа Фибоначчи:
если 0≤a,b≤9 — последние цифры чисел Fi и Fi+1 соответственно, то (a+b)mod10 — последняя цифра числа Fi+2

Sample Input:
875577

Sample Output:
2

"""


def fib_digit(n):
    a = 0
    b = 1
    while n != 0:
        a, b = b, (a + b) % 10
        n -= 1
    return a


if __name__ == '__main__':
    print(fib_digit(int(input())))
