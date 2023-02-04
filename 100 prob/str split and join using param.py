def split_and_join(line):
    # write your code here
    cut = line.split(" ")
    joined = "-".join(cut)
    return joined

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
# print(split_and_join('I am fine now'))