#Find Nth Fiboseq and also N fibo numbers
n = int(input())
a = 0
b = 1
c = a+b
seq  = []
seq.append(a)
seq.append(b)
seq.append(c)

for i in range(n-3):
    a  = b
    b = c
    c = a+b
    seq.append(c)
print(c)
print(seq)

#slow af
def fibonaciRecurs(n):
    if n<=1:
        return n
    else:
        return fibonaciRecurs(n-1) + fibonaciRecurs(n-2)

print(fibonaciRecurs(3))