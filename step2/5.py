try :
    h, m = input().split()
    H = int(h)
    M = int(m)

    if H not in range(0, 24) or M not in range(0, 60) :
        exit()
    
    if H == 0 and M < 45 :
        print("23 " + abs(M-45))
    elif M < 45 :
        print(H-1, abs(M-45))
    else :
        print(H, M-45)
except :
    print("입력이 잘못되었습니다")