onepoint = list(map(int,input("Enter the first point in x,y format: ").split(',')))
otherpoint = list(map(int,input("Enter the first point in x,y format: ").split(',')))
x1 = onepoint[0]
y1 = onepoint[1]
x2 = otherpoint[0]
y2 = otherpoint[1]

distance = ((x2-x1)**2 + (y2-y1)**2)**(1/2)
print(f" Distance between {(x1,y1)} and {(x2,y2)} is {distance} units") 