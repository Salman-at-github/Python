import time
data = []

t1 = time.time()
print("T1: ",t1)
for element in range(1,101):
    data.append(f"Element{element}")
t2 = time.time()
print("T2: ",t2)
print("Time taken is: ",t2-t1)
print(data)
print(time.clock_gettime())