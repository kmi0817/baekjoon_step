# (runtime: 254ms, memory: 17.1MB)
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        
        mins = [x for x in nums[0::2]]
        return sum(mins)