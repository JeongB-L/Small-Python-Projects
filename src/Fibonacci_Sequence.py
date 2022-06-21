#    Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.

all_fibo = []

def fibonacci(n1, n2, loop):
    value = 0
    for a in range(0, loop):
        value = n1 + n2
        n1 = n2
        n2 = value
        all_fibo.append(n2)
    return value
if '__main__' == __name__:
    while True:
        n = input("nth fibonacci number, enter n: ")
        if (n.isdigit()):
            break
    n = int(n)
    all_fibo.append(0)
    all_fibo.append(1)
    fibonacci_value = fibonacci(0, 1, n - 2)
    print(all_fibo)
    print(f'The {n}\'th fibonacci number is {fibonacci_value}')
