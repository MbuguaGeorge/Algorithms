"""
Binary Search algorithm is a type of search algorithm that works by 
dividing the dataset in half until the element is found.
It's more suitable compared to linear search.

Binary search algorithm has a time complexity of O(logn).

Below, I try and implement binary search with two methods.
1.Recursive
2.Iterative

"""

# 1. Recursve method
def binarysearchRecursive(x:int, arr:list, start:int, end:int) -> bool:

    if (start > end): # means that the values in the array are exhausted and we have not found our element.
        return False

    mid = int((start + end) / 2) #index of the midpoint
    
    # If at any point our midpoint is the element being searched, then we have our value
    if(arr[mid] == x): 
        return True
    elif (x > arr[mid]): #search the right side
        return binarysearchRecursive(x, arr, mid+1, end)
    elif (x < arr[mid]): #search the left side
        return binarysearchRecursive(x, arr, start, mid-1)


# 2. Iterative
def binarysearchIterative(x:int, arr:list, start:int, end:int) -> bool:

    while (start <= end):
        mid = int((start + end) / 2) 

        if(arr[mid] == x): 
            return True
        elif (x > arr[mid]):
            start = mid + 1
        elif (x < arr[mid]):
            end = mid - 1
    return False

if __name__ == '__main__':

    """
    How the algorithm works. Example:
    Say you have an array [11,20,21,34,50] and you are searching the element 34. *Note* Array must be sorted
    Divide array in half you get 21 as the midpoint.
    Now 21 is less than 34, that means our element will be on the right side of the array.
    Exclude every element on the left side including the mid point. We get an array [34,50]. 
    Now if the first element is chosen as the mid point, then we have our element.

    """

    #Test case 1
    arr = [1,2,3,4,5,6,7,8,9]
    start = 0
    end = len(arr) - 1
    print(binarysearchRecursive(2,arr,start,end))

    #Test case 2
    arr = [1,2,3,4,5,6,7,8,9]
    start = 0
    end = len(arr) - 1
    print(binarysearchIterative(12,arr,start,end))