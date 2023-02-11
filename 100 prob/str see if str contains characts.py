s = input("Enter the string: ")
lowerCase = []
upperCase = []
digits = '1234567890'
numbers = list(digits)
abc = 'abcdefghijklmnopqrstuvwxyz'
ABC = abc.upper()

for i in abc:
    lowerCase.append(i)
for i in ABC:
    upperCase.append(i)
    
low = False
upp = False
num = False
for char in s:
    for l in lowerCase:
        if l==char:
            low = True
    for L in upperCase:
        if L==char:
            upp = True
    for n in numbers:
        if n == char:
            num = True

# alphaNumeric = False
# justAlpha = False
# justNumeric = False
# justLower = False
# justUpper = False

# if low and upp and num or low and num or upp and num:
#     alphaNumeric = True
# print("Status is alphn: ",alphaNumeric)
# if low and upp and not num:
#     justAlpha = True
# print("Status is jal: ",justAlpha)
# if num and not low and not upp:
#     justNumeric = True
# print("Status is jnum : ",justNumeric)
    
# if low and not upp and not num:
#     justLower = True
# print("Status is:jlow ",justLower)
    
# if upp and not low and not num:
#     justUpper = True
# print("Status is:jupp ",justUpper)

# HACKERRANK PROBLEM (SEE IF GIVEN STRING CONTAINS ANY CHAR OF ALNUM,APHA,ISDIGIT,ISUPPER,ISLOWER)
fline = False
secline = False
thline = False
frline = False
fifline = False

for a in s:
    if a in lowerCase or a in upperCase or a in numbers:
        fline = True
    if a in lowerCase or a in upperCase:
        secline = True
    if a in numbers:
        thline = True
    if a in lowerCase:
        frline = True
    if a in upperCase:
        fifline = True

print(fline)
print(secline)
print(thline)
print(frline)
print(fifline)

