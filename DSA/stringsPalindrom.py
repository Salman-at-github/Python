# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

#  Certainly! Here's the code implementation of the algorithm described:

def isPalindrome(s):
    s = s.lower() #convert everything to lowercase
    startInd = 0
    endInd = len(s) -1
    while startInd < endInd:
        #skip the non alnum chars from start and end of str
        while startInd < endInd and not (s[startInd].isalnum()):
            startInd += 1
            
        while startInd < endInd and not (s[endInd].isalnum()):
            endInd -= 1
            
        #now done with non alnum, so compare the alnum
        if s[startInd]!=s[endInd]: #last and first elements should match continuesly for isPalindrome
            return False
        
        #transverse the string after every iter
        startInd+=1
        endInd-=1   
    return True #if all the above restrictions passed successfully, its a palindrome
    

print(isPalindrome("A man, a plan, a canal: Panama"))

# You can now call the `isPalindrome` function and pass your string `s` as an argument to check whether it is a palindrome:

# ```python
# string = "A man, a plan, a canal: Panama"
# print(isPalindrome(string))  # Output: True

# string = "race a car"
# print(isPalindrome(string))  # Output: False
# ```

# In the first example, the string "A man, a plan, a canal: Panama" is a palindrome after converting to lowercase and removing non-alphanumeric characters. Therefore, the function returns `True`. In the second example, the string "race a car" is not a palindrome, so the function returns `False`.