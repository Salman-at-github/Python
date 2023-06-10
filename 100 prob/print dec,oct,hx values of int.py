n = int(input())
width = len(bin(n))-2 #for last number's len

for i in range(1,n+1):
    string = "" #empty string (!string)
    for numSystem in "doXb": #4 num systems
        if string:   #check if string has any value, only then add space
            string+=" "
        formatPattern = "{:>" + str(width) + numSystem + "}" #create format(concat): "{:>" means align to right
        string+= formatPattern
    print(string.format(i,i,i,i))