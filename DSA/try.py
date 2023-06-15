#                                       O(log n)



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

print(isAnagram("rate","eatr"))




    