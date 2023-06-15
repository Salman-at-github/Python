# Q: Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# Here's the code with line-by-line explanations:

# ```python

#                                       O(n)
def isValid(s):
    stack = []  # Create an empty stack to store opening brackets
    bracket_map = {')': '(', '}': '{', ']': '['}  # Mapping of closing to opening brackets
    
    for char in s:  # Iterate over each character in the input string
        if char in bracket_map:  # If the character is a closing bracket
            top_element = stack.pop() if stack else '#'  # Get the top element from the stack, or use '#' if stack is empty
            if bracket_map[char] != top_element:  # Check if the closing bracket matches the most recent opening bracket
                return False  # If not, the string is not valid
        else:
            stack.append(char)  # If the character is an opening bracket, push it onto the stack
    
    return not stack  # The string is valid if the stack is empty after processing all characters


# ```

# Let's go through the code step by step:

# 1. The function `isValid(s)` takes an input string `s` as a parameter and returns a boolean indicating whether the string is valid or not.

# 2. We initialize an empty stack, `stack`, which will store the opening brackets.

# 3. We create a `bracket_map` dictionary that maps each closing bracket to its corresponding opening bracket.

# 4. We iterate over each character in the input string using a `for` loop.

# 5. Inside the loop, we check if the current character, `char`, is a closing bracket by using `if char in bracket_map:`.

# 6. If it is a closing bracket, we retrieve the top element from the stack using `stack.pop()` if the stack is not empty (`stack`) or use '#' as a sentinel value if the stack is empty. We store this element in the variable `top_element`.

# 7. We compare `top_element` with the corresponding opening bracket for the current closing bracket using `bracket_map[char] != top_element`. If they don't match, it means the brackets are not closed in the correct order or the closing bracket does not correspond to the most recent opening bracket. In this case, we return `False` as the string is not valid.

# 8. If the current character is not a closing bracket, it must be an opening bracket. We simply push it onto the stack using `stack.append(char)`.

# 9. After processing all characters in the input string, we check if the stack is empty using `not stack`. If the stack is empty, it means all opening brackets were properly closed, and the string is valid. We return `True`. Otherwise, if the stack is not empty, there are opening brackets that were not closed, and the string is not valid. We return `False`.

# This algorithm has a time complexity of O(n), where n is the length of the input string. It traverses the string once and performs constant-time operations for each character.