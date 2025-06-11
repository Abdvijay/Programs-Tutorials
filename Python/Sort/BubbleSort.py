def sort(nums):
    for i in range(1,len(nums)+1):
        for j in range(0,len(nums) - i):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j + 1] = temp

nums = [43,54,34,21,22,14]
print(nums)
sort(nums)
print(nums)