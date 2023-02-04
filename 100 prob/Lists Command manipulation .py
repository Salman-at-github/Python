#Command manipulation (lists)
# commands:

# insert i e: Insert integer e at position i.
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.

theList = []
n = int(input('Enter the Number of commands:'))
for i in range(n):
    commandList = input().split()
    print(commandList)
    if commandList[0] == 'insert':
        theList.insert(int(commandList[2]), commandList[1]) #list.insert(at position y, insert x)
    elif commandList[0] == 'print':
        print(theList)
    elif commandList[0] == 'remove':
        theList.remove(int(commandList[1])) #list.remove(x)
    elif commandList[0] == 'append': 
        theList.append(int(commandList[1])) #list.append(x)
    elif commandList[0] == 'sort':
        theList.sort() #sorting
    elif commandList[0] == 'pop':
        theList.pop() #pop last itme
    elif commandList[0] == 'reverse':
        theList.reverse() #reverse
print(theList)
    