#given an array, find the sub array with max sum (non contiguous)


#                                       My way (with lil help) (O(n))
def getMaxSubArrR(arr):
    currentSum = 0
    highestSubArr = []
    allNegative = True
    for num in arr:
        if num>=0:
            currentSum+=num
            highestSubArr.append(num)
            allNegative = False
        else:
            if currentSum < num:
                highestSubArr.append(num)
                currentSum = num
    if allNegative:
        currentSum = max(arr)
        highestSubArr = [currentSum]
    return highestSubArr, currentSum

print(getMaxSubArrR([8,3,-4,-6]))
