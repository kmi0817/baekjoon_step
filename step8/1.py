A, B, C = map(int, input().split())

if A < 1 or A > 2100000000 :
    print("A is between 1 ~ 2100000000")
    exit()
elif B < 1 or B > 2100000000 :
    print("B is between 1 ~ 2100000000")
    exit()
elif C < 1 or C > 2100000000 :
    print("C is between 1 ~ 2100000000")

sales_price = C
production_price = A + (B * 10)
break_even_point = 1

while sales_price <= production_price :
    sales_price += C
    break_even_point += 1

print(break_even_point)