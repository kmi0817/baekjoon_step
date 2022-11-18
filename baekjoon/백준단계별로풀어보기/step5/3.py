# 방법1) count() 직접 구현
def my_count(res) :
    count_list = list()

    for i in range(10) :
        cnt = 0
        for c in res :
            if str(i) == c :
                cnt += 1
        count_list.append(cnt)

    return count_list

A = int(input())
B = int(input())
C = int(input())

result = A * B * C
cnt_list = my_count(str(result))
for e in cnt_list :
    print(e)

# 방법2) count() 내장 함수 사용
A = int(input())
B = int(input())
C = int(input())

if A in range(100, 1000) and B in range(100, 1000) and C in range(100, 1000) :
    res = A * B * C

    for i in range(10) :
        print(str(res).count(str(i)))