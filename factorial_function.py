"""
Factorial function has a time complexity of O(n!).

"""

def factorial(n:int):
    if (n == 0):
        print('*')
        return
    
    x = 0

    while x < n:
        factorial(n-1)
        x += 1

if __name__ == '__main__':
    #Test case1
    factorial(4) #prints 24 stars
    print("Test case 2 begins here")
    #Test Case2
    factorial(3) #prints 6 stars