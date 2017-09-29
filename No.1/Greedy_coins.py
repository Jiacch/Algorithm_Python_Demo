# -*- coding:utf-8 -*-
# 有如下面值的硬币 现在输入一个数值 求出与之匹配的硬币数
conins = [1, 5, 10, 50, 100, 500]


def conins_list(A, input):
    for i in range(len(conins)-1, -1, -1):
        current_number = min(input[i], A/conins[i])
        A -= current_number * conins[i]
        print "{0},{1}".format(conins[i], current_number)
        pass

def main():
    # conins number
    input = [10, 10, 10, 10, 3, 1]
    aimed_number = 138

    conins_list(aimed_number, input)
    pass

if __name__ == '__main__':
    main()