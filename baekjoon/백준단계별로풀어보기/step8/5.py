test_case = int(input())
for i in range(test_case) :
    h, w, n = map(int, input().split())

    if h < 1 or w > 99 or n < 1 or h * w < n :
        print("Check range")
        exit()

    if n % h == 0 :
        floor = h
        room = n // h
    else :
        floor = n % h
        room = n // h + 1

    if room < 10 :
        print(f'{floor}0{room}')
        
    else :
        print(f'{floor}{room}')
