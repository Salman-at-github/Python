
#Given an array  of alphabets, if there is any vowel, find the number of letters between the first and last occurence of that vowel, if its present only once, print none, if not present even once, print absent.
vowels = list("aeiou")
# print(vowels)

wordList = list(input("Enter the word: "))
# print(wordList)

# aCount = 0
# eCount = 0
# iCount = 0
# oCount = 0
# uCount = 0
# for index,char in enumerate(wordList) :
#     if char in vowels:
#         print(f"{char} present")
#         if char =="a":
#             aCount+=1
#         elif char== "e":
#             eCount+=1
#         elif char== "i":
#             iCount+=1
#         elif char== "o":
#             oCount+=1
#         elif char== "u":
#             uCount+=1
#     if aCount > 1 or eCount > 1 or iCount > 1 or oCount > 1 or uCount > 1:
#         print(f"{char} is present {}")

currentEle = ""
count = 0
for v in vowels:
    if v in wordList:
        for index, char in enumerate(wordList):
            if char == v:
                print(f"{char} {index}")
                if char == currentEle:
                    count+=1

                else:
                    currentEle = char
                    count+=1

                if count>=2:
                    print(f'{currentEle} is found {count - 1} times')

    else:
        print(f"{v} not present")
    print("Count is ",count)