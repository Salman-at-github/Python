#1                                                  Iterative Method O(n)

def reverseList(arr,startIndice, endIndice):
    while startIndice < endIndice:
        arr[startIndice], arr[endIndice] = arr[endIndice], arr[startIndice] #this swaps the values without overwriting them unlike aobve two lines we can use temp to use the above two lins instead: 
        startIndice+=1
        endIndice-=1
    return arr

# A = [1, 2, 3, 4, 5, 6]
# print(A)
# result = reverseList(A, 0, 5)
# print("Reversed list is")
# print(result)


#                                                       Recursion O(n)
def reverseArr(arr, startI,endI ):
    if startI >= endI: #SET LIMIT to RECURSION
        return arr
    arr[startI], arr[endI] = arr[endI], arr[startI] #swap elements
    return reverseArr(arr, startI+1, endI-1) #call rec incresing the indices
    
# A = [9, 9, 3, 4, 5, 6]
# print(A)
# b = reverseArr(A, 0, 5)
# print("Reversed list is")
# print(b)


#                                                           List Slicing O(n)

def reverseArrLS(arr):
    return arr[::-1]

print(reverseArrLS([1,2,3,4,5,6,7]))
