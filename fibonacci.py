"""
Fibonacci series has a time complexity of O(2**n)
To be precise it actually is O(2**n-1) but we ignore constants.

In the code below I have implemented memoization so as to speed the execution of the program.

"""

memo = {}
def fib(n:int) -> int:
    if n in memo:
        return memo[n]
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        value = fib(n-1) + fib(n-2)
    memo[n] = value
    return value

if __name__ == '__main__':

    """
    *How it works*
                        fib(4)
                    /          \
                fib(3)        fib(2)
                /   \          /   \
            fib(2)   fib(1) fib(1)  fib(0)
            /   \
        fib(1) fib(0)

    """

    #Test case 1
    print(fib(4))

    #Test case 2
    print(fib(10))