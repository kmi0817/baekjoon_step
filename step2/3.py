try :
    year = int(input())

    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) :
        print("1")
    else :
        print("0")

    # 또 다른 방법
    # if year % 4 == 0 :
    #     if year % 100 != 0 or year % 400 == 0 :
    #         print("1")
    #     else :
    #         print("0")
    # else :
    #     print("0")

except :
    print("입력이 잘못되었습니다.")