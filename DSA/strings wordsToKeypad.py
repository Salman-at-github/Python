# Given a sentence in the form of a string, convert it into its equivalent mobile numeric keypad sequence. 

#                                           Using Dict O(n)
def sentenceToKeypadSequence(sentence):
    keypad_mapping = {
        'A': '2', 'B': '2', 'C': '2',
        'D': '3', 'E': '3', 'F': '3',
        'G': '4', 'H': '4', 'I': '4',
        'J': '5', 'K': '5', 'L': '5',
        'M': '6', 'N': '6', 'O': '6',
        'P': '7', 'Q': '7', 'R': '7', 'S': '7',
        'T': '8', 'U': '8', 'V': '8',
        'W': '9', 'X': '9', 'Y': '9', 'Z': '9'
    }

    keypad_sequence = ""
    sentence = sentence.upper()  # Convert the sentence to uppercase to handle both lowercase and uppercase characters

    for char in sentence:
        if char in keypad_mapping:
            keypad_sequence += keypad_mapping[char]

    return keypad_sequence


# Explanation:

# We define the function sentenceToKeypadSequence that takes the input sentence as a parameter.

# We create a dictionary keypad_mapping that maps each character to its corresponding keypad digit. The letters are mapped to their respective digits on a standard mobile phone keypad.

# We initialize an empty string keypad_sequence that will store the resulting keypad sequence.

# We convert the sentence to uppercase using the upper() method. This is done to handle both lowercase and uppercase characters consistently.

# We iterate through each character char in the sentence.

# Inside the loop, we check if the character is present in the keypad_mapping dictionary using the in operator.

# If the character is present in the mapping, we append the corresponding keypad digit to the keypad_sequence string using the += operator.

# After the loop ends, we have the complete keypad sequence stored in the keypad_sequence string.

# Finally, we return the keypad_sequence, which represents the equivalent mobile numeric keypad sequence of the input sentence.

# The time complexity of this algorithm is O(n), where n is the length of the input sentence. We iterate through each character in the sentence exactly once.

# The auxiliary space complexity is O(1) because we only use a constant amount of space to store the keypad sequence and the keypad mapping dictionary, which has a fixed size.



#                                       Using Array O(n)
def printSequence(arr, input):

    # length of input string
    n = len(input)
    output = ""

    for i in range(n):

        # checking for space
        if(input[i] == ' '):
            output = output + "0"
        else:
            # calculating index for each
            # character
            position = ord(input[i]) - ord('A')
            output = output + arr[position]
    # output sequence
    return output


# Driver code
str = ["2", "22", "222",
       "3", "33", "333",
       "4", "44", "444",
       "5", "55", "555",
       "6", "66", "666",
       "7", "77", "777", "7777",
       "8", "88", "888",
       "9", "99", "999", "9999"]

input = "GEEKSFORGEEKS"
print(printSequence(str, input))