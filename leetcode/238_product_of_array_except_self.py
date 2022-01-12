class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if 0 in nums :
            if nums.count(0) > 1 :
                return [0 for i in range(len(nums))]
            else : # nums.count(0) == 1
                result = [0 for i in range(len(nums))]
                
                index_of_zero = nums.index(0)
                product = 1
                for n in nums[:index_of_zero] + nums[index_of_zero + 1:] :
                    product *= n
                result[index_of_zero] = product
                return result
            
        else :
            result = []
            product = 1
            for n in nums :
                product *= n
            for n in nums :
                result.append(product // n)
            return result