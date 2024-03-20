nums = [1,4,6,7,2,6,8]
target = 3
stack = [5,4,3,7,8,9]

def two_sum (nums, target):
    for i in range(len(nums)):
        print ("IIIIIII is " , nums[i])
        for j in range(i+1, len(nums)):
            print ("OOOOOOO is " , nums[j])
            k = nums[i] + nums[j]
            print (f"KKKKKK is {k}")
            if k== target:                
                print(f"YESSSSSSSSSS {i} {j}")
            # else:
            #     print ("NOOOOOOOO")





# print ("Length is " , len(nums))
# print (f"Range is {range(len(nums))}")

# print (f"Range is {range(1,2)}")

# print (f"Nums Index 0 is {nums[0]}")

# print (f"Nums Index 1 is {nums[1]}")

# print (f"Nums Index 8 is {nums[len(nums)-1]}")

print (two_sum(nums, target))

nums.append(9)
print (nums)

print (f"Stack is {stack}")
stack.pop()
stack.append(1)
print (f"Stack is {stack}")
stack.pop()
print (f"Stack is {stack}")