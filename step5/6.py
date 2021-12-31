import sys

n = int(input())

for i in range(n) :
    ox = sys.stdin.readline().rstrip()

    final_score = 0
    serial_o = 0
    for c in ox :
        if c == "O" :
            serial_o += 1
            final_score += serial_o

        elif c == "X" :
            serial_o = 0
    print(final_score)