X = int(input())
if X < 1 or X > 10000000 :
    print('X should be between 1 and 10,000,000')

left, right = 0, 1
section  = 1

# 1) Find the section where X is in.
while X not in range(left, right + 1) :
    section = section + 1
    left = right + 1
    right = right + section

# 2) Find X's index in the section
section_range = [x for x in range(left, right+1)]
X_index = section_range.index(X)

# 3) Set the amount
# amount = min(X_index, len(section_range) - X_index)

# print(f'X index = {X_index}')
# print(f'section = {section}')
# print(f'amount = {amount}')

# 4) Find denominator (분모) and numerator (분자)
if section % 2 == 1 :
    denominator = section - X_index
    numerator = 1 + X_index
else :
    denominator = 1 + X_index
    numerator = section - X_index

print(f'{denominator}/{numerator}')