nameList = input().split()
print(nameList)
capFName = ""
for word in nameList:
    capFName+=word.capitalize()+" "
print(capFName[0:-1]) #removes the extra last space
