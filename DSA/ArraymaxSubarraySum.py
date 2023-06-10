#From an array, find highest sum contiguous subrray (contiguous mean continues index)

def maxSubArray(nums):
    max_sum = float('-inf')
    current_sum = 0
    start = 0
    end = 0
    temp_start = 0
#[2,3,-5,1]
    for i, num in enumerate(nums):
        if current_sum + num < num:
            current_sum = num
            temp_start = i
        else:
            current_sum += num

        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i

    return max_sum, nums[start:end + 1]

# Kadane's Algorithm:

# The algorithm initializes max_sum and current_sum to negative infinity and 0, respectively. These variables keep track of the maximum subarray sum seen so far and the current sum of the subarray being examined.
# The start and end variables are used to track the indices of the subarray with the maximum sum.
# The algorithm iterates through the input array nums using a loop. For each element, it compares whether adding the current element to the current sum (current_sum + num) would result in a larger sum than just the current element (num). If the former is true, it includes the current element in the subarray; otherwise, it starts a new subarray from the current element.
# At each iteration, the algorithm updates max_sum if the current sum is greater. It also updates the start and end indices accordingly.
# Finally, the algorithm returns max_sum as the maximum subarray sum and uses slice notation (nums[start:end + 1]) to return the corresponding subarray.
# The enumerate() function is a built-in Python function that allows you to iterate over a sequence (such as a list, tuple, or string) while also tracking the index of each element in the sequence. It returns an iterator that generates pairs of indices and values.

# enumerate(sequence, start=0)

#  eg fruits = ['apple', 'banana', 'orange']
# for index, fruit in enumerate(fruits):
#     print(index, fruit)
