croatia_alphabet = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
check_alphabet = ["c", "d", "l", "n", "s", "z"] # z, j 제외

S = input()

total_length = len(S)
special_cnt = 0
for index, c in enumerate(S) :
    if c in check_alphabet :
        if c == "d" and S[index+1] == "z" :
            test_alphabet = 
        c_and_next = S[index:]

        if c_and_next in croatia_alphabet :
            special_cnt += 1
print(len(S) - special_cnt)