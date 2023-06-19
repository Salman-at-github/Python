#Given a string S. For each index i(1<=i<=N-1), erase it if s[i] is equal to s[i-1] in the string.
#
def removeConsecutiveCharacter(S):
    stack = []  # Initialize an empty stack to store characters

    for char in S:
        if len(stack) > 0 and char == stack[-1]:
            stack.pop()  # Remove the top element from the stack if it matches the current character
        else:
            stack.append(char)  # Push the current character onto the stack

    modified_string = ''.join(stack)  # Convert the stack into a string

    return modified_string


# To solve the given problem, we can use a stack data structure. We iterate through each character in the string and compare it with the top element of the stack. If they are equal, we pop the top element from the stack; otherwise, we push the current character onto the stack.
# Explanation:

# We define the function removeConsecutiveCharacter that takes the input string S as a parameter.

# We create an empty stack using the list data structure and assign it to the variable stack.

# We iterate through each character char in the input string S.

# Inside the loop, we check if the stack is not empty (len(stack) > 0) and if the current character char is equal to the top element of the stack (char == stack[-1]).

# If the condition is true, it means the current character is consecutive to the previous character. Therefore, we remove the top element from the stack using the pop() function, effectively erasing the consecutive occurrence.

# If the condition is false, it means the current character is not consecutive to the previous character. In this case, we push the current character onto the stack using the append() function.

# After the loop ends, we have the modified string with consecutive characters removed stored in the stack.

# Finally, we convert the stack into a string by joining its elements together using the join() function and assign the result to the variable modified_string.

# We return the modified_string, which represents the final output.

# The time complexity of this algorithm is O(|S|), where |S| is the length of the input string. This is because we iterate through each character in the string exactly once.

# The auxiliary space complexity is also O(|S|) because, in the worst case, the stack can hold all the characters of the input string.