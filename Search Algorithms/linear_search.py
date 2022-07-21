"""
Linear search has a time complexity of O(n).

It works by looking at every single item in a list until it finds a match

"""

def linear_search(arr:list, target:int) -> int:

    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return None

def verify(index):
    if index is not None:
        print('Target found at: ', index)
    else:
        print('Target not found')

if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7,8,9]
    result = linear_search(arr, 8)
    verify(result)

    result = linear_search(arr, 40)
    verify(result)