def make_newScore(m, score_list) :
    new_score_list = list()

    for score in score_list :
        new_score_list.append(score/m*100)

    return new_score_list

def make_avg(score_list) :
    return sum(score_list)/len(score_list)

N = int(input())
if N > 1000 or N < 0 :
    exit()

original_score_list = list(map(int, input().split()))
if len(original_score_list) != N :
    exit()


# # 100보다 작거나 같은 수
# if a > 100 or b > 100 or c > 100 :
#     exit()
# # 음수 아닌 정수
# elif a < 0 or b < 0 or c < 0 :
#     exit()
# # 적어도 하나의 값은 0보다 크다
# elif a == 0 and b == 0 and c == 0 :
#     exit()

# abc_list = [a, b, c]
M = max(original_score_list)

new_score_list = make_newScore(M, original_score_list)
print(make_avg(new_score_list))
