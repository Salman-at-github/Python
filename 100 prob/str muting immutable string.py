def mutate_string(string, position, character):
    lis = list(string)
    lis[position] = character
    joinedString = ''.join(lis)
    return joinedString

if __name__ == '__main__':
    s = input("Enter the string: ")
    i, c = input(f"Enter the {i,c}: ").split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)