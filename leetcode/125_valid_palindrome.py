# 1) use string slicing (runtime: 40ms, memory: 15.2MB)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_list = []
        for char in s.lower():
            if char.isalnum() :
                s_list.append(char)

        updated_s = "".join(s_list)
        return updated_s == updated_s[::-1]

# 2) use list (runtime: 268ms, memory: 14.9MB)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        s_list = []
        for char in s:
            if char.isalnum() :
                s_list.append(char)

        is_palindrome = True
        while True :
            try :
                left_char = s_list.pop(0)
                right_char = s_list.pop()
            except IndexError :
                break

            if left_char != right_char :
                is_palindrome = False
                break
                
        return is_palindrome

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s_list = []
#         for char in s:
#             if char.isalnum() :
#                 s_list.append(char.lower())

#         is_palindrome = True
#         while len(s_list) > 1 :
#             if s_list.pop(0) != s_list.pop() :
#                 is_palindrome = False
#                 break
#         return is_palindrome