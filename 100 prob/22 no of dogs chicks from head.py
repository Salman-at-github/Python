tot = int(input("Enter the total number of heads: "))
legs = int(input("Enter the total number of legs: "))
if tot%2==0 and legs%2==0:
    d = (legs//2) - tot
    c = tot - d
    print(f"There are about {d} dogs and {c} chickens!")
    if d<0 or c<0:
        print('Negative numbers mean you have entered wrong data assumption')
else:
    print("That's not the right numbers! The numbers must be even!")