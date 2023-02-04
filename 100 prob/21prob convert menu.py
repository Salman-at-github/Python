num = int(input("""Choose a number from the following options:
                1 - for cm to ft
                2 - for km to miles
                3 - for USD to INR
                4 - to exit
                """))
if num==1:
    cm = int(input("Enter the cm to convert to ft: "))
    ft = cm/30.48
    print(f"{cm} cm is {ft} ft")
elif num==2:
    km = int(input("Enter the km to convert to miles: "))
    miles = km/1.609
    print(f"{km} km is {miles} miles")
elif num == 3:
    USD = int(input("Enter the USD to convert to INR: "))
    INR = USD*81.55
    print(f"{USD} USD is {INR} INR")
elif num==4:
    exit()
else:
    print('Enter a correct option')