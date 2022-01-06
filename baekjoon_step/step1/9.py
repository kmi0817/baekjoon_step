try :
    a, b = input().split()
    A = int(a)
    B = int(b)

    if A >= 1 and B <= 10000 :
        print(A+B)
        print(A-B)
        print(A*B)
        print(A//B)
        print(A%B)
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except :
    print("정수를 입력하시오")

# try :
#     ab_list = input().split(" ")
#     A = int(ab_list[0])
#     B = int(ab_list[1])

#     if A >= 1 and B <= 10000 :
#         print(A+B)
#         print(A-B)
#         print(A*B)
#         print(A//B)
#         print(A%B)
# except ZeroDivisionError :
#     print("0으로 나눌 수 없습니다.")
# except :
#     print("정수를 입력하세요.")
