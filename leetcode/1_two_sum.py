# 1) for and in (list) (runtime: 965ms, 14.9MB)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, a in enumerate(nums) :
            # a + b = target
            b = target - a
            
            if b in nums and nums.index(b) != i :
                return [i, nums.index(b)]

# 2) two for (runtime: 2504ms, memory: 14.9MB)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)) :
            # a + b = target
            b = target - nums[i]
            
            for j in range(i+1, len(nums)) :
                if nums[j] == b :
                    return [i, j]

# 3) for and while (runtime: 9366ms, memory: 14.9MB)               
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ret_list = []
        for a_index, a in enumerate(nums) :
            # A (=digit) + B = target
            b = target - a
            
            b_index = a_index + 1
            while b_index < len(nums) :
                if nums[b_index] == b :
                    ret_list.append(a_index)
                    ret_list.append(b_index)
                    break
                b_index += 1
                
        return ret_list