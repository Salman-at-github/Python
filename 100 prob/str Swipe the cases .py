def swap(s):
    word = ''
    for i in s:
        if i==i.lower():
            i= i.upper()
            word += i
        elif i==i.upper():
            i = i.lower()
            word += i
    return word

print(swap('SalMan'))