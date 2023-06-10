#                                           ROTATE TO RIGHT (On)
def reverseArr(arr, IndexStart, IndexEnd):
    while IndexStart < IndexEnd:
        arr[IndexStart],arr[IndexEnd] = arr[IndexEnd], arr[IndexStart]
        IndexStart +=1
        IndexEnd -=1
    return arr

def rotateArrayRight(arr, i): #rotate to right i elements
    arrSize = len(arr)
    i = i%arrSize
    #first reverse entire array
    reverseArr(arr, 0, arrSize-1) #0 to 4
    
    #reverse before i
    reverseArr(arr, 0, i-1) #0 to 1

    
    #at last reverse from i till end
    reverseArr(arr, i, arrSize-1) #2 to 4
    return arr

print(rotateArrayRight([1,2,3,4,5], 2))


#Principle: First reserve entire array (0 to size-1), then reverse smaller part (0 to i-1), at last reverse the remaining bigger part (i to size-1)


#                                       ROTATE TO LEFT (On)
def reverseArr2(arr, startI, endI):
    while startI < endI:
        arr[startI],arr[endI] = arr[endI],arr[startI]
        startI+=1
        endI-=1

def rotateArrLeft(arr,i):
    arrSize = len(arr)
    i = i % arrSize #makes sure even if i is greater than array, it adjusts
    #first reverse entire array
    reverseArr2(arr, 0, arrSize-1) #0 to 4 (5)
    #reverse the bigger part of arr
    reverseArr2(arr, 0, (arrSize-i) - 1) #0 to 2 (3)
    #reverse smaller part
    reverseArr2(arr, arrSize-i, arrSize -1 ) #3 to 4 (2)
    return arr
print()
print(rotateArrLeft([1,2,3,4,5], 2))

#Principle: First rotate entire arr (0 to arrSize-1), then reverse bigger part of arr (0 to (arrSize-i)-1), and at last reverse the smaller part ((arrSize-i) to arrSize-1)

#[1,2,3,4,5,6]: i = 3, so size-i = 6-3 = 3 = (0 to 2), then 3 to 5
