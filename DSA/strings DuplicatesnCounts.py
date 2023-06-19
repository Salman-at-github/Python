# Write an efficient program to print all the duplicates and their counts in the input string 
# To efficiently print all the duplicates and their counts in an input string, we can use a dictionary to keep track of the frequency of each character. Then, we iterate through the characters in the string, update their frequencies in the dictionary, and print the duplicates with their counts.

# Here's the code with a line-by-line explanation:

# ```python

#                                           Using Dict O(n)
def printDuplicatesd(input_string):
    char_frequency = {}

    # Count the frequency of each character
    for char in input_string:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1

    # Print duplicates and their counts
    for char, frequency in char_frequency.items():
        if frequency > 1:
            print(char, frequency)

printDuplicatesd("aaaaabbcccdff")
# ```

# Explanation:

# 1. We define the function `printDuplicates` that takes the input string as a parameter.

# 2. We create an empty dictionary `char_frequency` to store the frequency of each character.

# 3. We iterate through each character `char` in the input string.

# 4. Inside the loop, we check if the character is already present in the `char_frequency` dictionary.

# 5. If the character is already present, we increment its frequency by 1 using `char_frequency[char] += 1`.

# 6. If the character is not present, we add it to the `char_frequency` dictionary with a frequency of 1 using `char_frequency[char] = 1`.

# 7. After counting the frequency of each character, we iterate through the items in the `char_frequency` dictionary using the `items()` method.

# 8. Inside the loop, we check if the frequency of the character is greater than 1 using `frequency > 1`.

# 9. If the frequency is greater than 1, it means the character is a duplicate. We print the character and its frequency using the `print()` function.

# By using the dictionary to count the frequency of each character, we avoid redundant iterations over the input string and achieve an efficient solution. The time complexity of this algorithm is O(n), where n is the length of the input string, because we iterate through each character of the string exactly once.

# The auxiliary space complexity is O(k), where k is the number of unique characters in the input string. In the worst case, if all characters in the input string are unique, the dictionary `char_frequency` will store k key-value pairs. However, in the best case, if there are no duplicates, the space usage would be O(1) as the dictionary would be empty except for a few unique characters.


#                                   using Sort time: O(n logn), space: O(1)    
def printDuplicates(str):
    # Converting string to list of characters
    char_list = list(str)
    # Sorting the list of characters
    char_list.sort()
     
    # Loop through the sorted list to find duplicates
    i = 0
    while i < len(char_list):
        count = 1
        # Counting the occurrences of each character
        while i < len(char_list)-1 and char_list[i] == char_list[i+1]:
            count += 1
            i += 1
         
        # Printing the duplicate character and its count
        if count > 1:
            print(char_list[i], ", count = ", count)
        i += 1
 
str = "test string"
printDuplicates(str)
# Output
# s, count = 2
# t, count = 3
# Explanation for the above code:

# Initialize the input string str to a given string of characters from a to z.
# Find the length of the input string str using the length() function of the string class
# Sort the string using the sort() function from the <algorithm> library. Sorting brings all duplicate characters together and makes it easier to count their occurrences.
# Loop through the sorted string character by character.
# For each character, count the number of times it occurs in the string by looping over the subsequent characters until a different character is found.
# If the count of the current character is greater than 1, print the character and its count.
# Continue looping until all characters have been processed.
# Exit the loop and terminate the program
# Time Complexity: O(nlogn), where n is the length of the string 

# Space Complexity: O(1), if you observe we did not use any extra space .    

#                                            (Best)
#                                   Using bit manipulation T: O(n), S: O(1)
MAX_CHAR = 26  # Maximum number of characters
 
 
def print_duplicates(string):
    bit_vector = 0  # Initialize the bit vector to zero
    # Initialize an array to keep track of character counts
    char_counts = [0] * MAX_CHAR
 
    for char in string:
        # Get the bit index for the current character
        bit_index = ord(char) - ord('a')
        if bit_index < 0:
            continue  # Skip characters that are not lowercase letters
        if not (bit_vector & (1 << bit_index)):  # Check if the bit is already set
            bit_vector |= (1 << bit_index)  # Set the bit
        else:
            # Increment the count for the duplicate character
            char_counts[bit_index] += 1
 
    for i in range(MAX_CHAR):
        if char_counts[i] > 0:
            # Get the character corresponding to the current bit index
            c = chr(i + ord('a'))
            # Print the duplicate character and its count
            print(f"{c}, count = {char_counts[i] + 1}")
 
 
# Example usage
string = "test string"
print_duplicates(string)
# Output
# s, count = 2
# t, count = 3
# Explanation of the above code:

# We declare a constant MAX_CHAR to store the maximum number of characters. Here, it is set to 26 because we are working with lowercase English alphabets.
# We define a function printDuplicates which takes the input string str as a parameter. Inside this function, we initialize a variable bitVector to zero, which will be used to
# keep track of which characters have occurred more than once, and an array charCounts to keep track of the occurrence count of each character.
# We iterate through each character in the string using a for loop. For each character, we calculate the bit index by subtracting the ASCII value of the character ‘a’ from
# its ASCII value. This gives us the index of the bit that corresponds to the character in the bit vector.
# We then check whether the bit is already set in the bit vector using the bitwise & operator. If it is not set, we set the bit by using the bitwise | operator.
# If the bit is already set, we increment the count for the duplicate character in the charCounts array.
# After processing all characters in the string, we iterate through the charCounts array and print the duplicate characters along with their count if the count is greater
# than zero. We use the i index to get the character corresponding to the current bit index, and we add 1 to the count because we already counted the first occurrence
# of the character in the bitVector.
# Finally, we define the main function which initializes the input string str, prints a message to indicate which string is being processed, and calls the printDuplicates function
#  Time complexity: O(n), The time complexity is O( n), where n is the length of the input string. 

# space complexity: O(1), Because we are not using any extra space.