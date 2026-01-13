#Find second largest number in a list
nums = [10, 20, 4, 45, 99, 99]
numss = list(set(nums)) #to remove duplicates
numss.sort()
print(numss[-2])  # 45

nums.sort(reverse=True)
print(nums[1])  # 20