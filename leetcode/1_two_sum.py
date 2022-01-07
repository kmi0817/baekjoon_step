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