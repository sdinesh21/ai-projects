# Problem: Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# Input: nums = [4,1,2,1,2]
# Output: 4

def singleOccurence(nums):
    num_count = {}
    count = 0
    for num in nums:
        if num in num_count:
            num_count[num] += 1
        else:
            num_count[num] = 1
    for num, count in num_count.items():
        if count == 1:
            return num


nums = [4,1,2,1,2]
print (singleOccurence(nums))