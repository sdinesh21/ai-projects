# Problem: Given a list of integers, write a function that moves all 0's to the end of it while maintaining the relative order of the non-zero elements. Do this in-place without making a copy of the array.
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]


def moveZero (nums):
    pos = 0
    for i in range(len(nums)):
        print (f"I is {i}")
        if nums[i] != 0:
            # print (f"nums[Pos] is {nums[pos]}")
            # print (f"nums[i] is {nums[i]}")
            nums[pos], nums[i] = nums[i],  nums[pos]
            print(nums)
            pos+=1

nums = [0,1,0,3,12]
moveZero(nums)
print(nums)