N = int(input())
if N < 1 or N > 1000000000 :
    print("N should be between 1 and 1,000,000,000")

rooms = 1
start_num = 1
end_num = 1
n = 0 # 6n (n >= 1) & 1 (n = 0)

while N not in range(start_num, end_num + 1) :
    n = n + 6
    rooms = rooms + 1
    start_num = end_num
    end_num = end_num + n

print(rooms)