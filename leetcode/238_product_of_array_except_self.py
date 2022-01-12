class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_cnt = nums.count(0)
        
        if zero_cnt == 1 :
            product_except_self = [0 for i in range(len(nums))]
            index_of_zero = nums.index(0)
            product_result = 1
            for n in (nums[0:index_of_zero] + nums[index_of_zero + 1:]) :
                product_result *= n
            product_except_self[index_of_zero] = product_result
            return product_except_self
            
        elif zero_cnt > 1 :
            return [0 for x in range(len(nums))]
        
        else :
            product_result = 1
            for n in nums :
                product_result *= n
            
            product_except_self = []
            for n in nums :
                product_except_self.append(product_result // n)
            return product_except_self