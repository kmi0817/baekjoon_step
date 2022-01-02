croatia_alphabet = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
check_alphabet = ["c", "d", "l", "n", "s", "z"] # z, j 제외

###
S = input()

total_length = len(S)
special_cnt = 0
for i in range(len(S)) :
    if S[i] in check_alphabet :
        char_2 = S[i:i+2]
        char_3 = S[i:i+3]

        if char_3 == "dz=" :
            special_cnt +=1
        elif char_2 in croatia_alphabet :
            special_cnt += 1
print(total_length - special_cnt)
