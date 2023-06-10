def gcd(a,b):
    if b==0:
        return a
    return gcd(b, a%b)

print(gcd(3918848, 1653264))


#Logic: Eucleadian algorithm says that gcd can be found by assigning a = b, and b = remainder of a/b. Once remained becomes 0, the prev remainder is the gcd. Here's an example of how the Euclidean algorithm works to find the GCD of 24 and 18:
# Divide 24 by 18 to get a quotient of 1 and a remainder of 6.
# Set 24 to be 18 and 18 to be 6 (the remainder from the previous step).
# Divide 18 by 6 to get a quotient of 3 and a remainder of 0.
# The last non-zero remainder was 6, so the GCD of 24 and 18 is 6.
#another eg. (10,5)
#            (5,10/5)
#            (5,0)