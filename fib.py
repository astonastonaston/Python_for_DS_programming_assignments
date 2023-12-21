
def fibonacci(n):
    """
    Input: The number of Fibonacci numbers to compute \n
    Return: The list of first-n fib numbers
    """
    assert type(n)==int
    assert n>0
    fn1, fn2, nxt = 1, 1, 3
    for i in range(n):
        yield fn1 # assign but not return at creation. Same variable values!
        fn2, fn1 = fn1+fn2, fn2


def main():
    print(list(fibonacci(10)))
    return 0

main()