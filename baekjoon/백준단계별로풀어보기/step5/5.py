# 점수/M*100 만드는 함수 (M: 최대값)
def make_newScore(m, score_list) :
    new_score_list = list()

    for score in score_list :
        new_score_list.append(score/m*100)

    return new_score_list

# 평균 구하는 함수
def make_avg(score_list) :
    return sum(score_list)/len(score_list)


# 과목 개수 입력
N = int(input())
if N > 1000 or N < 0 :
    exit()

# 과목별 점수 입력
original_score_list = list(map(int, input().split()))
if len(original_score_list) != N :
    exit()

# 과목 내 최대값 구하기
M = max(original_score_list)

# 함수 적용 및 출력
new_score_list = make_newScore(M, original_score_list)
print(make_avg(new_score_list))
