n, m, y, x, k = [int(x) for x in input().split()]
pan = []
for i in range(n):
    pan.append([int(x) for x in input().split()])
cmds = [int(x) for x in input().split()]
cube = [0]*7
for cmd in cmds:
    is_valid = False
    old_cube = cube.copy()
    if cmd == 1 and x < m-1:  # e
        cube[1] = old_cube[4]
        cube[2] = old_cube[2]
        cube[3] = old_cube[1]
        cube[4] = old_cube[6]
        cube[5] = old_cube[5]
        cube[6] = old_cube[3]
        x += 1
        is_valid = True
    elif cmd == 2 and x > 0:  # w
        cube[1] = old_cube[3]
        cube[2] = old_cube[2]
        cube[3] = old_cube[6]
        cube[4] = old_cube[1]
        cube[5] = old_cube[5]
        cube[6] = old_cube[4]
        x -= 1
        is_valid = True
    elif cmd == 3 and y > 0:  # n
        cube[1] = old_cube[5]
        cube[2] = old_cube[1]
        cube[3] = old_cube[3]
        cube[4] = old_cube[4]
        cube[5] = old_cube[6]
        cube[6] = old_cube[2]
        y -= 1
        is_valid = True
    elif cmd == 4 and y < n-1:  # s
        cube[1] = old_cube[2]
        cube[2] = old_cube[6]
        cube[3] = old_cube[3]
        cube[4] = old_cube[4]
        cube[5] = old_cube[1]
        cube[6] = old_cube[5]
        y += 1
        is_valid = True

    if is_valid:
        # print(y, x)
        if pan[y][x] == 0:
            pan[y][x] = cube[6]
        else:
            cube[6] = pan[y][x]
            pan[y][x] = 0
        print(cube[1])
