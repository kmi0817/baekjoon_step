class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3 :
            return []

        ret_list = []
        for i, a in enumerate(nums) :
            for j, b in enumerate(nums[i+1:]) :
                temp_c = 0 - (a+b)
                if temp_c in nums[i+j+2:] :
                    triplet = sorted([a, b, temp_c])
                    if triplet not in ret_list :
                        ret_list.append(triplet)
        return ret_list