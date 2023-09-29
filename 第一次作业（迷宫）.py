import random

def maze_build():
    def dfs(x, y):
        if x < 1 or x >= 9 or y < 1 or y >= 9 or maze[x][y] == 1:
            return
        maze[x][y] = 1
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            dfs(x + dx, y + dy)

    maze = [[0 for j in range(10)] for i in range(10)]
    while True:
        entrance = random.choice([(0, i) for i in range(1, 9)] + [(i, 0) for i in range(1, 9)] + [(i, 9) for i in range(1, 9)])
        exit = random.choice([(0, i) for i in range(1, 9)] + [(i, 0) for i in range(1, 9)] + [(i, 9) for i in range(1, 9)])
        if entrance[0] != exit[0] and entrance[1] != exit[1]:
            maze[entrance[0]][entrance[1]] = 2
            maze[exit[0]][exit[1]] = 8
            dfs(entrance[0], entrance[1])
            break

    return maze

def print_maze(maze, current_position):
    for i in range(10):
        for j in range(10):
            if (i, j) == current_position:
                print("5", end=" ")
            elif maze[i][j] == 0:
                print("0", end=" ")
            elif maze[i][j] == 1:
                print("1", end=" ")
            elif maze[i][j] == 2:
                print("2", end=" ")
            elif maze[i][j] == 8:
                print("8", end=" ")
        print()

def move(maze, current_position, direction):
    x, y = current_position
    if direction == 'W':
        new_x, new_y = x - 1, y
    elif direction == 'S':
        new_x, new_y = x + 1, y
    elif direction == 'A':
        new_x, new_y = x, y - 1
    elif direction == 'D':
        new_x, new_y = x, y + 1

    if 0 <= new_x < 10 and 0 <= new_y < 10 and maze[new_x][new_y] != 0:
        maze[x][y] = 1
        maze[new_x][new_y] = 5
        return (new_x, new_y)
    else:
        return current_position

maze = maze_build()
current_position = (2, 1)  
print_maze(maze, current_position)

while True:
    direction = input("Enter W, S, A, D to move (or Q to quit): ").upper()
    if direction == 'Q':
        break
    current_position = move(maze, current_position, direction)
    print_maze(maze, current_position)
    if maze[current_position[0]][current_position[1]] == 8:
        print("Congratulations! You have reached the exit.")
        break
##因为昨天复阳了，吊了一天水，所以基本上没学什么，代码是ChatGPT跑的，我调试了几遍不能实现功能，但是因为基础薄弱暂时找不出解决办法，后面等身体恢复了会尽快解题的！