# -*- coding:UTF-8 -*-

import Queue

# input init()
m = 10
n = 10
maze = [
    '#S######.#',
    '......#..#',
    '.#.##.##.#',
    '.#........',
    '##.##.####',
    '....#....#',
    '.#######.#',
    '....#.....',
    '.####.###.',
    '....#...G#',
]
maze = [ list(maze[x]) for x in range(len(maze))]

INF = 100000000
MAX = 20
arr = list()

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

point = dict().fromkeys(['x', 'y'])

# start point && end point
sx = 0
sy = 1
gx = 9
gy = 8

def BFS():
    q = Queue.Queue(maxsize=INF)
    for i in range(0, MAX):
        arr.append(list())
        for j in range(0, MAX):
            arr[i].append(INF)
    q.put((sx, sy))
    arr[sx][sy] = 0

    while q.qsize():
        top_point = q.get()
        if top_point[0]==gx and top_point[1]==gy:
            break
        for i in range(0,4):
            nextx = top_point[0] + dx[i]
            nexty = top_point[1] + dy[i]
            if nextx>=0 and nextx<n and nexty>=0 and nexty<m and \
                maze[nextx][nexty]!='#' and arr[nextx][nexty]==INF:
                q.put((nextx, nexty))
                arr[nextx][nexty] = arr[top_point[0]][top_point[1]] + 1
                maze[nextx][nexty] = arr[nextx][nexty]
    return arr[gx][gy]
    pass

def main():
    print BFS()
    pass

if __name__ == '__main__':
    main()