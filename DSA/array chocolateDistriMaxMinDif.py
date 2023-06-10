# Given an array of N integers where each value represents the number of chocolates in a packet. Each packet can have a variable number of chocolates. There are m students, the task is to distribute chocolate packets such that: 

# Each student gets one packet.
# The difference between the number of chocolates in the packet with maximum chocolates and the packet with minimum chocolates given to the students is minimum.

def minimum_difference(arr, m):
    # Sort the array in ascending order
    arr.sort()

    n = len(arr)
    min_difference = float('inf')

    # Find the minimum difference by iterating through the array
    start = 0
    end = m - 1
    while end < n: #while end < lenght of array
        difference = arr[end] - arr[start]
        if difference < min_difference:
            min_difference = difference
        start += 1
        end += 1

    return min_difference


# Sort the array of chocolate packets in ascending order. Sorting helps in finding the minimum difference as it allows us to compare adjacent packets easily. We can use any efficient sorting algorithm like quicksort or mergesort.

# Initialize the necessary variables. We start by setting the minimum difference (min_difference) to a very large value, initially infinity. This ensures that any difference we find in the subsequent steps will be smaller than the initial value.

# Iterate through the array using a sliding window approach. We will move the window from left to right, considering different combinations of packets.

# In each iteration, calculate the difference between the chocolate packets at the "end" and "start" indices. The "end" index represents the right end of the window, and the "start" index represents the left end of the window. This difference will give us the difference in the number of chocolates between the maximum and minimum packets in the current window.

# Check if the current difference is smaller than the current minimum difference (min_difference). If it is, update the value of min_difference with the new, smaller difference.

# Move the window by incrementing both the "start" and "end" indices. This step allows us to consider the next window of packets in the array.

# Repeat steps 4-6 until we reach the end of the array, making sure that the window size remains equal to the number of students (m).

# Finally, return the value of min_difference, which represents the minimum difference between the maximum and minimum number of chocolates given to the students.

