#                                 Using Sort (not the best)

def getMinMaxS(arr):
    arr.sort()
    max = arr[-1]
    min = arr[0]
    obj = {"max" : max, "min" : min}
    return obj

result = getMinMaxS([2,1,5,8])
print(f'Maximum is {result["max"]} and min {result["min"]}')


#                               Using Linear Search (all elements transversed)

def getMinMaxL(arr):
    maxi = arr[0]
    mini = arr[0]
    for i in range(1,len(arr)):
        if arr[i]>max:
            max = arr[i]
        if arr[i]<min:
            min = arr[i]
    result = {"max": max, "min" : min}
    return result

array = [4,9,0,2,3]
# print(getMinMaxL(array))


#                                                     Using Recursion (Best 1)
#Principal: If one el in arr, max and min is same, elif two el, then compare and assing max and min, if more than two el, break the arr into half and apply the same thorugh recursion until the array has only one or two elements and then return the result

def getMinMaxR(lowestIndice,highestIndice,arr):
    maximumVal = arr[lowestIndice]
    minVal = arr[lowestIndice]


    if lowestIndice == highestIndice: #if only one ele
        maximumVal = arr[lowestIndice]
        minVal = arr[lowestIndice]
        return(maximumVal, minVal)

    #elif highestIndice == lowestIndice + 1
    elif lowestIndice + highestIndice == 1: #if only two elements
        if arr[highestIndice] > arr[lowestIndice]:
            maximumVal = arr[highestIndice]
            minVal = arr[lowestIndice]
        else:
            maximumVal = arr[lowestIndice]
            minVal = arr[highestIndice]
        return(minVal, maximumVal)
    else:#more than two el, breakdown through recur
        mid = int((lowestIndice+highestIndice)/2)
        firstHalfMaxVal, firstHalfMinVal = getMinMaxR(lowestIndice, mid, arr)
        secHalfMaxVal , secHalfMinVal = getMinMaxR(mid+1 , highestIndice, arr)
    return (max(firstHalfMaxVal, secHalfMaxVal), min(firstHalfMinVal, secHalfMinVal))

arrayy = [4,5,9,1]
low = 0
high = len(arrayy) - 1
maximum, minimum = getMinMaxR(low, high, arrayy)
# print(f'{maximum} >>> {minimum}')



#                                                       Pair Wise Comparison (Best 2)
def getMinMaxp(arr):
    n = len(arr)
    if n%2!=0: #if n odd
        maxi = arr[0]
        mini = arr[0]
        i = 1
    else: #if even
        maxi = arr[0]
        mini = arr[1]
        i = 2
    while i< (n-1):
        if arr[i] > arr[i+1]:
            maxi = max(maxi, arr[i])
            mini = min(mini, arr[i+1])
        else:
            maxi = max(maxi, arr[i+1])
            mini = min(mini, arr[i])
        i+=2 #increase by two as its pair wise comparison
    return (maxi, mini)
    
# print(getMinMaxp([1,9,0,20]))



#                                                     using infinity Linear comparison

def getMinMaxinfinity(arr):
    #if no array
    if not arr:
        return None
    
    #set min = greatest, max = lowest for comparison in loop
    minimumVal = float('inf')
    maximumVal = float('-inf')

    #compare and set the value
    for element in arr:
        if element < minimumVal:
            minimumVal = element
        if element > maximumVal:
            maximumVal = element
    return minimumVal, maximumVal 

numz = [2,1,4,5,45,5,6,90]
print(getMinMaxinfinity(numz))

