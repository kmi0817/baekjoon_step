def make_str_2_list(string) :
    ret_list = list()
    for c in string :
        ret_list.append(c)

    return ret_list

###
A, B = input().split()

reversed_A_list = reversed(make_str_2_list(A))
reversed_B_list = reversed(make_str_2_list(B))

reversed_A_str = "".join(reversed_A_list)
reversed_B_str = "".join(reversed_B_list)

reversed_A = int(reversed_A_str)
reversed_B = int(reversed_B_str)

print(max([reversed_A, reversed_B]))
