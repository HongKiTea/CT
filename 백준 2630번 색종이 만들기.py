maxSquareSize = int(input())
s = []
for i in range(maxSquareSize):
    s.append(list(map(int, input().split())))

b_num = 0
w_num = 0

# ss : square size
def check_square(x, y, ss):
    global w_num, b_num

    c = s[x][y]
    for i in range(x, x + ss):
        for j in range(y, y + ss):
            if c != s[i][j]:
                n_ss = ss // 2
                check_square(x, y, n_ss)
                check_square(x + n_ss, y, n_ss)
                check_square(x, y + n_ss, n_ss)
                check_square(x + n_ss, y + n_ss, n_ss)
                return
    if c == 0:
        w_num += 1
    else:
        b_num += 1
    return

check_square(0, 0, maxSquareSize)
print(w_num)
print(b_num)