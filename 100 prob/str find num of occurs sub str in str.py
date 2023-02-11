str = input("Enter the str: ")
subStr = input("Enter sub: ")
size = len(subStr)
matches = 0
for i in range(len(str)):
        # print("Str portion is: ",str[i:i+size])
        # print("sub str is: ",subStr)
        if str[i:i+size] == subStr: #String from a[0:to size needed] (last number of 0:x, x is not taken, only x-1)
            matches+=1
        else:
            pass
print("Total matches = ",matches)