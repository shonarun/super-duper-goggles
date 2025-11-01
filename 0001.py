nums : list = [2,7,11,15]
target : int = 9
n = len(nums)
for i in range(n):
    comp = target - nums[i]
    if comp in nums:
        result = [i, nums.index(comp)]

print(result)