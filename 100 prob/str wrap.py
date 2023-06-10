string = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
max_width = int(input("Enter the max length: "))
start = 0
end = max_width
cycle = 0
if (len(string)//max_width)!=len(string)/max_width:
    cycle += (len(string)//max_width)+1
else:
    cycle+=len(string)//max_width
increaseBy = max_width

newstring = ""
for i in range(cycle):
    portion = string[start:end]
    newstring+=portion+"\n"
    start +=increaseBy
    end +=increaseBy
print(newstring)


