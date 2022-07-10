"""
MergeSort is an example of a divide and conquer type of algoritm.
It works by dividing the dataset into half recursively till you have a single element in the array.

The time complexity of mergesort is O(nlogn)

*Explained*
The dataset is divided into two recursively for a number of times. That is O(logn)
Each element is iterated over and compared with one another. That is O(n)
Therefore, you have O(n*logn) -> O(nlogn).

"""

def mergesort(arr:list) -> list:
    # The array is returned when you have only one element left. Because one element in an array is already sorted.
    if (len(arr) < 2):
        return arr

    mid = int((len(arr))/2)
    leftarr = arr[:mid] #elements from index 0 till mid. Excluding mid.
    rigtharr = arr[mid:] #elements from the mid to the end of the array. Incuding mid.

    return merge(mergesort(leftarr), mergesort(rigtharr))

def merge(leftarr:list, rightarr:list) -> list:
    resultarr = []
    rightindex = 0 #keeps track of values on the rightarr
    leftindex = 0 #keeps track of values on the leftarr
    
    while (len(leftarr) > leftindex and len(rightarr) > rightindex):    #The loop terminates when either the left or right array is exhausted
        if (leftarr[leftindex] < rightarr[rightindex]):
            resultarr.append(leftarr[leftindex])
            leftindex += 1
        else:
            resultarr.append(rightarr[rightindex])
            rightindex += 1

    #The following while loops are supposed to take care of the items remaining 
    # in either the rightarr or leftarr when the above while loop terminates
    while leftindex < len(leftarr):
        resultarr.append(leftarr[leftindex])
        leftindex += 1
    
    while rightindex < len(rightarr):
        resultarr.append(rightarr[rightindex])
        rightindex += 1

    return resultarr 

if __name__ == '__main__':
    
    """
    How the merge function works. Example*
    Say you have 2 arrays; leftarr [7,3] and rightarr [4,1,8].
    The first while loop compares the elements in these two arrays and adds the smallest element into an empty array.
    The first while terminates when the leftarr is exhausted and we remain with one element in the rightarr.
    That's where the two arrays come in. They check either the rightarr or leftarr 
    for a remaining value and add it to the empty array, now filled with values.

    """

    # Test case 1
    arr = [10,5,2,7,4,9,12,1,8,6,11,3]
    print(mergesort(arr))

    #Test case 2
    arr = [100,24,673,36,6,19,57,32,50,36,36]
    print(mergesort(arr))