class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3 :
            return []
        
        nums.sort()
        ret_list = []
        for i in range(len(nums) - 2) :
            if i > 0 and nums[i] == nums[i-1] :
                continue

            left, right = i + 1, len(nums) - 1
            while left < right :
                temp_sum = nums[i] + nums[left] + nums[right]
                if temp_sum > 0 :
                    right -= 1
                elif temp_sum < 0 :
                    left += 1
                else :
                    if [nums[i], nums[left], nums[right]] not in ret_list :
                        ret_list.append([nums[i], nums[left], nums[right]])
                    right -= 1
                    left += 1
        return ret_list