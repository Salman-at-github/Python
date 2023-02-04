from array import array
if __name__ == '__main__':
    n = int(input("Enter no. of students: "))
    arr = array("i", sorted(list(map(int, input(" Enter the scores in a sequence separated by space: ").split(" ")))))
    for i in range(n):
        if arr[i] > arr[i-1]:
            runner_up = arr[i-1]
    print(f"The runner up is: {runner_up}")
