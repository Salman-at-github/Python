#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

def duplicateExists(arr):
    comparedAlready = []
    for item in arr:
        if item in comparedAlready:
            return True
        else:
            comparedAlready.append(item)
    return False
print(duplicateExists([1,2,3,5,4,5]))  #used the idea hashset for list here (copied)


#                                           Best One (On)Hashset data structure
def containsDuplicateHS(nums):
    num_set = set()
    for num in nums:
        if num in num_set:
            return True
        else:
            num_set.add(num)
    return False






