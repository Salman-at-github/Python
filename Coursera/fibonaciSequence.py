#Find Nth Fiboseq 

import sys #max digits can be printed is 4.3k, so use sys to aloow bigger

sys.set_int_max_str_digits(10000000)

n = int(input())
a = 0
b = 1
c = a+b
if n == 1:
    print(a)
elif n == 2:
    print(b)
else:
    for i in range(n-3):
        a  = b
        b = c
        c = a+b
    print(c)

