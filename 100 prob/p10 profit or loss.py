cost = float(input("Enter the cost of the item: "))
sell = float(input("Enter the selling price of the item: "))

if (sell-cost)>0:
    print(f"It is a profit of {sell-cost} rupees.")
elif (sell-cost)<0:
    print(f"It is a loss of {sell-cost} rupees.")
else:
    print('Neither profit nor loss')
    