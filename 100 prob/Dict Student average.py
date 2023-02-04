n = int(input("Enter the number of students: "))

#Creating DB
dataBase= {} #dictionary to store the key pair values
for i in range(n):
    name = input("Enter name: ")
    score = list(map(float, input().split())) #list of student score, mapped to float
    dataBase[name] = score #assigning the name and the score to dictionary (dict[key]=value)

#Findint the student and their avg
query = input("Enter the student name you wanna check on: ") #student to be found
if query in dataBase: #if student found in db
    scores = dataBase[query]
    m = len(scores) #no of scores
    avg = sum(scores)/m
    roundedAvg = '%.2f' % avg #format to 2 decimals as per question
    print(f"Average of {query} is {roundedAvg}")
else:
    print(f"No such student named '{query}' found in Database")

