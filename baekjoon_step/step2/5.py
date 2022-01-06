try :
    h, m = input().split()
    H = int(h)
    M = int(m)
    if M > 45 and M < 59 :
        print(H, M-45)
    elif M == 45 :
        print(H, 0)
    else :
        if H == 0 :
            H = 24
        print(H-1, 60+(M-45))

except :
    print("입력이 잘못되었습니다.")
