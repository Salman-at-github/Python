import time
data = []

t1 = time.time()
print("T1: ",t1)
for element in range(1,10000001):
    data.append(f"Element{element}")
t2 = time.time()
print("T2: ",t2)
print(data)
print("Time taken is: ",t2-t1)