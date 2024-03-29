# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

#my solution
def ValidAnagram(string,targetString):
    mainStrList = list(string.lower())
    targetstrList = list(targetString.lower())
    for element in targetstrList:
        if element not in mainStrList:
            return False

    return True

# print(ValidAnagram("Bruh","hubr"))
#Principle: convert both strings into list, then search the targetstrlist elements in mainstrList, if all are found then return true else false
#Result:  your algorithm does not take into account the count of each character. In an anagram, the counts of characters in both strings should be the same. Your algorithm only checks for the presence of characters, but it does not handle cases where characters occur multiple times or when the counts of characters are different. Therefore, your algorithm is not correctly solving the anagram problem.



#                                   O(n)
def isAnagram(s,t):
    if len(s) != len(t): #if both str lenght not same then its not an anagram
        return False
    #create an array of 26 elements to store count of 26 alphabet chars
    count = [0] *26

    #store the appearance of each char in Mainstr using ord to count array
    for char in s:
        index = ord(char) - ord("a")
        count[index]+=1
    print(count)
    #now for each similar char present in t, decrease the count value
    for char in t:
        index = ord(char) - ord("a")

        count[index]-=1
    print(count)
    #if any value != 0 in count then its not an anagram
    for value in count:
        if value!=0:
            return False
    return True

print(isAnagram("bruh","hubr"))
# Here's an explanation of each line in the updated  code:

# ``` 
# def isAnagram(s, t):
# ```
# This is the function definition. It takes two parameters, `s` and `t`, representing the input strings.

# ``` 
#     if len(s) != len(t):
#         return False
# ```
# This line checks if the lengths of `s` and `t` are equal. If they are not equal, it means that the strings cannot be anagrams, so the function returns `False`.

# ``` 
#     count = [0] * 26
# ```
# This line initializes an array called `count` with 26 elements, each initially set to 0. This array will be used to store the count of each letter in the English alphabet.

# ``` 
#     for char in s:
#         index = ord(char) - ord('a')
#         count[index] += 1
# ```
# These lines iterate over each character, `char`, in string `s`. The `ord(char) - ord('a')` expression calculates the index of the character in the `count` array by subtracting the ASCII value of `'a'` from the ASCII value of the current character. It then increments the count at that index.

# ``` 
#     for char in t:
#         index = ord(char) - ord('a')
#         count[index] -= 1
# ```
# These lines iterate over each character, `char`, in string `t`. Similar to the previous loop, it calculates the index of the character in the `count` array and decrements the count at that index.

# ``` 
#     for value in count:
#         if value != 0:
#             return False
# ```
# These lines iterate over each value in the `count` array. If any value is not zero, it means that the count of some letter is different between `s` and `t`, so the function returns `False`.

# ``` 
#     return True
# ```
# If all values in the `count` array are zero, it means that the counts of all letters are the same between `s` and `t`, so the function returns `True`, indicating that `t` is an anagram of `s`.

# I hope this explanation clarifies the functionality of each line in the code!

#Principle: First len of s = t. Create a matrix of 0*26 ele to store the presence of each alphabet, increase or decrease the value of the ele by 1 for every presence using index which is found using ord(char) - ord("a") that gives index 0 to 25. If char in mainstring, increase. If its in targetString, decrease. At last if all the ele are 0 in matrix, its an anagram. 