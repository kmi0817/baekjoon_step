from string import ascii_lowercase

S = input()

alphabet_list = list(ascii_lowercase)
for alphabet in alphabet_list :
    print(S.find(alphabet), end=" ")