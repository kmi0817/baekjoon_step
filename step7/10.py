import sys
N = int(input())

group_word_cnt = 0
for i in range(N) :
    exit_chars = list()
    former_char = ""
    is_group_word = True

    word = sys.stdin.readline().lower()

    for char in word :
        if char != former_char and char in exit_chars :
            is_group_word = False
            break
        elif char != former_char and char not in exit_chars :
            exit_chars.append(char)

        former_char = char
    
    if is_group_word :
        group_word_cnt += 1

print(group_word_cnt)
