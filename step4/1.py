import sys

try :
    result_list = list()
    while True :
        a, b = sys.stdin.readline().rstrip().split()
        A = int(a)
        B = int(b)

        if A == 0 and B == 0 :
            break
        elif A > 0 and B < 10 :
            result_list.append(A+B)
        else :
            print("A와 B의 범위가 맞지 않습니다.")

    for result in result_list :
        print(result)
except :
    print("문제가 발생했습니다.")