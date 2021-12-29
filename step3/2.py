try :
    cnt = int(input())

    ab_list = list()
    for i in range(cnt) :
        temp_a, temp_b = input().split()
        ab_list.append(int(temp_a))
        ab_list.append(int(temp_b))

    for i in range(0, cnt*2, 2) :
        print(ab_list[i] + ab_list[i+1])

except :
    print("입력이 잘못되었습니다")