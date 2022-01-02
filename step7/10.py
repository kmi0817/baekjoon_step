N = int(input())

exit_char = list()

former_char = ""
is_group_word = True
group_word_cnt = 0
for i in range(N) :
    word = input().lower()

    for char in word :
        if char == former_char :
            is_group_word = False
            break
        elif char in exit_char :
            is_group_word = False
            break
        else :
            exit_char.append(char)

    former_char = ""
    is_group_word = True
    exit_char.clear()
    if is_group_word :
        group_word_cnt += 1

print(group_word_cnt)
