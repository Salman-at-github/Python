# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity.

#                                         O(log n)

def findIndex(nums, target):
    startIndex = 0
    endIndex = len(nums) - 1

    while startIndex <= endIndex:
        mid = (startIndex + endIndex) // 2

        if nums[mid] == target:
            return mid

        if nums[startIndex] <= nums[mid]:  # left half is sorted
            if nums[startIndex] <= target <= nums[mid]:  # Target is within the left half
                endIndex = mid - 1
            else:
                startIndex = mid + 1
        else:  # right half is sorted
            if nums[mid] <= target <= nums[endIndex]:  # Target is within the right half
                startIndex = mid + 1
            else:
                endIndex = mid - 1

    return -1

print(findIndex([4,5,0,1,2,3],3)) 


# The findIndex function takes in two parameters: nums (the rotated sorted array) and target (the element we want to find the index of).
# We initialize two variables, left and right, which represent the indices at the left and right ends of the array, respectively.
# We use a while loop to perform a modified binary search on the array.
# Inside the loop, we calculate the middle index, mid, by finding the average of left and right.
# We check if the element at the middle index, nums[mid], is equal to the target element. If it is, we return the middle index.
# If the left half of the array is sorted (the value at left is less than or equal to the value at mid), we check if the target element is within the range of the left half. If it is, we update the right index to mid - 1 to search the left half of the array. Otherwise, we update the left index to mid + 1 to search the right half of the array.
# If the right half of the array is sorted (the value at mid is less than the value at right), we check if the target element is within the range of the right half. If it is, we update the left index to mid + 1 to search the right half of the array. Otherwise, we update the right index to mid - 1 to search the left half of the array.
# If we exit the while loop without finding the target element, we return -1 to indicate that it is not present in the array.
# In summary, the code performs a modified binary search on the rotated sorted array to find the index of the target element. It compares the target with the middle element and adjusts the search range based on whether the left or right half of the array is sorted.
