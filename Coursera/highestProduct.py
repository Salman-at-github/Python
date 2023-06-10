n = int(input())
nums = list(map(int, input().split()))
if n!=len(nums):
    print(f"Enter {len(nums)} numbers into the array!")
else:
    nums.sort()
    maxProd = nums[-1]*nums[-2]
    print(maxProd)
