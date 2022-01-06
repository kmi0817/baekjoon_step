s = input().lower() # make lower
s_list = []
for char in s:
    if char.isalpha() :
        s_list.append(char)
print(s_list)
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

print(is_palindrome)