def sort(nums):
    for i in range(0,len(nums)):
        minPos = i
        for j in range(i + 1,len(nums)):
            if nums[j] < nums[minPos]:
                minPos = j

        temp = nums[i]
        nums[i] = nums[minPos]
        nums[minPos] = temp  

nums = [43,54,34,21,22,14]
print(nums)
sort(nums)
print(nums)