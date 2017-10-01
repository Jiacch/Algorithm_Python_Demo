
def solve(N, L):
    ans = 0
    while N>1:
        mii1 = 0
        mii2 = 1
        if L[mii1]>L[mii2]:
            L[mii2], L[mii1] = L[mii1], L[mii2]
        for i in range(2, N, 1):
            if L[i]<L[mii1]:
                mii2 = mii1
                mii1 = i
            elif L[i]<L[mii2:
                mii2 = i
        t = L[mii1] + L [mii2]
        ans += t
        if mii1==N-1:
            mii1, mii2 = mii2, mii1
        L[mii1] = t
        L[mii2] = L[N-1]
        n -= 1
    print ans
    pass

def main():
    # input
    N = 3
    L = [8, 5, 8]

    ans = 0
    sorted(L)
    while N>1:
        min1 = 0
        min2 = 1
        t = L[min1] + L[min2]
        ans += t
        min1 += 1
        min2 += 1
        L[min1] = t
        N -= 1
    print ans
    pass

if __name__ == '__main__':
    main()