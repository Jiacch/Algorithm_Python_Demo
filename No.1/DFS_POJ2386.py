# -*- coding:UTF-8 -*-

# Lake Counting

# data input
m = 12
n = 10
input_arr = [
    'W........WW.',
    '.WWW.....WWW',
    '....WW...WW.',
    '.........WW.',
    '.........W..',
    '..W......W..',
    '.W.W.....WW.',
    'W.W.W.....W.',
    '.W.W......W.',
    '..W.......W.'
    ]
# arr = [ [] for i in range(len(input_arr))]
# for i in range(len(input_arr)):
#     for j in range(len(input_arr[i])):
#         arr[i].append(str(input_arr[i][j]))
arr = [ list(input_arr[x]) for x in range(len(input_arr))]

def DFS(i, j):
    arr[i][j] = '.'
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            newx = i + dx
            newy = j + dy
            if newx>=0 and newy>=0 and newx<n and newy<m and arr[newx][newy]=='W':
                DFS(newx, newy)
    return
    pass

def main():
    count = 0
    for x in range(0,n-1):
        for y in range(0, m-1):
            if arr[x][y] == 'W':
                DFS(x, y)
                count += 1
    print count
    pass

if __name__ == '__main__':
    main()