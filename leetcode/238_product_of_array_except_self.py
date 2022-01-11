class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_list = []
        for i in range(len(nums)) :
            array_except_i = list(map(str, nums[0:i] + nums[i+1:]))
            product_list.append(eval('*'.join(array_except_i)))
        return product_list