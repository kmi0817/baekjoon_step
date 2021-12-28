try :
    score = int(input())

    if score not in range(0, 101) :
        exit()
    
    if score in range(90, 101) :
        print("A")
    elif score in range(80, 90) :
        print("B")
    elif score in range(70, 80) :
        print("C")
    elif score in range(60, 70) :
        print("D")
    else :
        print("F")
except :
    print("입력이 잘못되었습니다.")