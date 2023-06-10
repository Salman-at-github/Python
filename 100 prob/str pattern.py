n,m = list(map(int,input("Enter Len x Wid: ").split(" ")))

if m%n!=0:
    print("Width must be a multiple of Length!")
else:
    if n%2==0:
        print("Lenth must be an odd number!")
    else:
        pattern = ".|."
        pattLen = len(pattern)
        pattMultiplier = 1
        dashes = "-"
        for i in range((n-1)//2):
            print((pattern*pattMultiplier).center(m,"-"))
            pattMultiplier+=2
        print("Welcome".center(m,"-"))
        for i in range((n-1)//2):
            print((pattern*(pattMultiplier-2)).center(m,"-"))
            pattMultiplier-=2

