try :
    T = int(input())

    ab_list = list()
    for i in range(T) :
        temp_a, temp_b = input().split()
        a = int(temp_a)
        b = int(temp_b)

        if a > 0 and b < 10 :
            ab_list.append([a, b])
        else :
            print("수의 범위를 확인해주세요.")

    for index, ab_pair in enumerate(ab_list, 1) :
        print("Case #" + str(index) + ": " + str(ab_pair[0]) + " + " + str(ab_pair[1]) + " = " + str(ab_pair[0] + ab_pair[1]))
except :
    print("입력이 잘못되었습니다.")