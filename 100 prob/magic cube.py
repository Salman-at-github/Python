import random
start = True

while start:
    mc = []
    num = list(range(1,10))
    random.shuffle(num)
    mat = [num[i:i+3] for i in range(0,9,3)]

    # Check that the matrix has no repeated numbers and all the numbers are in the range of 1 to 9
    if len(set(num)) == 9 and all(n in num for n in range(1, 10)):
        if mat[0][0]+mat[0][1]+mat[0][2]==15 and mat[1][0]+mat[1][1]+mat[1][2]==15 and mat[2][0]+mat[2][1]+mat[2][2]==15 and mat[0][0]+mat[1][1]+mat[2][2]==15 and mat[0][2]+mat[2][1]+mat[2][0]==15 and mat[0][0]+mat[1][0]+mat[2][0]==15 and mat[0][1]+mat[1][1]+mat[2][1]==15 and mat[0][2]+mat[1][2]+mat[2][2]==15:
            print(mat)
            mc = mat
            start = False
        print("Running..")


#for rows sum: if mat[0][0]+mat[0][1]+mat[0][2]==15 and mat[1][0]+mat[1][1]+mat[1][2]==15 and mat[2][0]+mat[2][1]+mat[2][2]==15
#for diagonals sum: mat[0][0]+mat[1][1]+mat[2][2]==15 and mat[0][2]+mat[2][1]+mat[2][0]==15
#for col sums: mat[0][0]+mat[1][0]+mat[2][0]==15 and mat[0][1]+mat[1][1]+mat[2][1]==15 and mat[0][2]+mat[1][2]+mat[2][2]==15:


#Will take long time to find the matrix as probability is 9/(9!)