try :
    h, m = input().split()
    H = int(h)
    M = int(m)

    if H not in range(0, 24) or M not in range(0, 60) :
        exit()
    
    # 이 코드는 자꾸 except으로 넘어감. 왜?...
    # if H == 0 and M < 45 :
    #     print("23 " + abs(M-45))
    if M < 45 :
        if H-1 < 0 :
            print(24 + (H-1), 60 - (45-M))
        else :
            print(H-1, 60 - (45-M))
    else :
        print(H, 60 - (45 - M))
except :
    print("입력이 잘못되었습니다")
