nums = [-1,0,1,2,-1,-4]
if not nums or len(nums) < 3 :
    print([])
    exit()

ret_set = set()
for i, a in enumerate(nums) :
    for j, b in enumerate(nums[i+1:]) :
        print(f'nums[i+1]: {nums[i+1:]}, a = {a}, b = {b}')
        temp_c = 0 - (a+b)
        if temp_c in nums[i+j+2:] :
            print(f'nums[i+j+2]: {nums[i+j+2:]}, c = {temp_c}')
            ret_set.add((a, b, temp_c))
print(list(ret_set))