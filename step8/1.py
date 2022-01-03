A, B, C = map(int, input().split())

# 입력 범위 제한
if A < 1 or A > 2100000000 :
    print("A is between 1 ~ 2100000000")
    exit()
elif B < 1 or B > 2100000000 :
    print("B is between 1 ~ 2100000000")
    exit()
elif C < 1 or C > 2100000000 :
    print("C is between 1 ~ 2100000000")
    exit()


if C <= B :
    print(-1)
else :
    print(A // (C-B) + 1)