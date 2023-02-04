angles = list(map(float, input('Enter the three angles separated by , in a,b,c format: ').split(',')))
# print(angles)

total = sum(angles)

if total==180:
    print("It's a triangle ")
else:
    print("It is not a triangle!")