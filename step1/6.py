try :
    A, B = input().split()
    A = int(A)
    B = int(B)

    if A > 0 and B < 10 :
        print(A-B)
except :
    print("정수를 입력하시오")

# try :
#     ab_list = input().split(" ")
#     A = int(ab_list[0])
#     B = int(ab_list[1])
# except :
#     print("정수를 입력하세요")

# try :
#     if A > 0 and B < 10 :
#         print(A - B)
# except :
#     print("문제가 발생했습니다.")
