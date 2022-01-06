from string import ascii_uppercase

S = input().upper()
alphabets = list(ascii_uppercase)

frequent = ""
cnt = 0
for alphabet in alphabets :
    temp_cnt = S.count(alphabet)

    if cnt < temp_cnt :
        cnt = temp_cnt
        frequent = alphabet
    elif cnt == temp_cnt :
        frequent = "?"

print(frequent)
