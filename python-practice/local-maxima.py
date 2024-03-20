def find_maxima(nums):
    maxima = set()
    for index, item in enumerate(nums):
        print (f"Index is {index} and Item is {item}")
        # print (len(nums))
        if (index+2 < len(nums)):
            if nums[index+1] >= item and nums[index+1] >= nums[index+2]:
                maxima.add(nums[index+1])
    return maxima
            






nums = [1,3,2,4,4,4,4]
print (find_maxima(nums)) # [3,4]

# 1. Iterate
# 2. If Value(i+1) > Value(i) and Value(i+1) > Value(i+2)
# 3. 