import csv

def divisorGenerator(n):
    for i in range(1,n//2+1):
        if n%i == 0: yield i

def is_perfect(n):
    """
    Input: Data and output file name\n
    Return: The list of first-n fib numbers
    """
    assert type(n)==int
    a = []
    for i in divisorGenerator(n):
        a.append(i)
    print(a)
    return (sum(a)==n)



# def main():
#     a=28
#     print(is_perfect(a))
#     return 0

# main()