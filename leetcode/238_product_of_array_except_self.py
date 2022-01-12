class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_all = 1
        for n in nums :
            if n != 0 :
                product_all *= n
            
        product_except_self = []
        for n in nums :
            if n != 0 :
                product_except_self.append(product_all//n)
            else :
                product_except_self.append(product_all)
            
        return product_except_self