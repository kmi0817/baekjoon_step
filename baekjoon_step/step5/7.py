import sys

def check_range(lis) :
    for e in lis:
        if e >= 0 and e <= 100 :
            ret = True
        else :
            print("점수의 범위가 틀렸습니다.")
            exit()
    return ret

def compute_avg(lis) :
    return sum(lis)/len(lis)

def compute_percentage(avg, lis) :
    higherScore_list = list()
    for e in lis :
        if e > avg :
            higherScore_list.append(e)

    return round(len(higherScore_list) / len(lis) * 100, 3)

###
C = int(input())

for i in range(C) :
    case = list(map(int, sys.stdin.readline().split()))
    
    std_N = case.pop(0) # 0번째 값 취득 및 삭제
    if check_range(case) :
        avg = compute_avg(case)
        above_avg_percentage = compute_percentage(avg, case)

        # print("{:.3f}%".format(above_avg_percentage))
        print(f"{above_avg_percentage:.3f}%")