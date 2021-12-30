target_N = int(input()) # 26

if target_N < 10 :
    left = 0
    right = target_N
else :
    left = int(str(target_N)[0]) # int 2
    right = int(str(target_N)[1]) # int 6
result = left + right # int 8

temp_N = int(str(right) + str(result)) # int 68

cnt = 1
while temp_N != target_N :
    saved_result = result # becomes 'right' soon 8
    result = right + result # int 14
    
    if result > 9 :
        result = int(str(result)[1]) # int 4
    right = saved_result # int 8

    temp_N = int(str(right) + str(result)) # int 84
    cnt += 1
print(cnt)
