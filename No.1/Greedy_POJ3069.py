

def main():
    # input
    N = 6
    R = 10
    x = [1, 7, 15, 20, 30, 50]
    count = 0
    i = 0
    sorted(x)
    while i<N:
        tmp = x[i]
        i += 1
        while i<N and x[i]<=tmp+R:
            i += 1
        tmp2 = x[i-1]
        while i<N and x[i]<=tmp2+R:
            i += 1
        count += 1
    print count
    pass

if __name__ == '__main__':
    main()