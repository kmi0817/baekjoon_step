import sys

try :
    T = int(input())

    ab_list = list()
    for i in range(T) :
        temp_a, temp_b = sys.stdin.readline().rstrip().split()
        a = int(temp_a)
        b = int(temp_b)

        if a >= 1 and a <= 1000 and b >= 1 and b <= 1000 :
            ab_list.append(a)
            ab_list.append(b)
        else :
            print("수의 범위를 확인하세요.")
            exit(1)
    
    for j in range(0, T*2, 2) :
        print(ab_list[j] + ab_list[j+1])
    

except :
    print('입력이 잘못되었습니다.')