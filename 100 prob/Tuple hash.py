#Task: Given an integer ,n , and n space-separated integers as input, create a tuple, t , of those  integers. Then compute and print the result of hash(t) .
#hash() returns the hash value, which is the integer used to find a key in the dictionary quickly

n = int(input("Enter how many elements?: "))
tup = tuple(map(int, input().split())) #create tuple

if len(tup)==n:
    print(hash(tup))
else: 
    size = len(tup)
    print(f"You entered {size} instead of {n} elements")
print(tup)

