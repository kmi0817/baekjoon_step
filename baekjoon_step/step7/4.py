T = int(input())
if T < 1 or T > 1000 :
    print("1<= T <= 1,000")
    exit()

for i in range(T) :
    R, S = input().split()
    R = int(R)

    if R < 1 or R > 8 :
        exit()
    if len(S) < 1 or len(S) > 20 :
        exit()

    new_str = ""
    for c in S :
        new_str += c * R
    print(new_str)