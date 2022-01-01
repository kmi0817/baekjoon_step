S = input().strip()
if len(S) > 1000000 or len(S) < 1 :
    exit()

S_list = S.split()
print(len(S_list))
