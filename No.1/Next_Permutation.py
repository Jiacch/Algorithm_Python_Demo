
num = [1,2,3,4,5]

def nextPermutation(num):
    if len(num) <= 1:
        return num
    for i in range(len(num)-2, -1, -1):
        if num[i] < num[i+1]:
            j = i + 1
            while j < len(num):
                if num[i] >= num[j]:
                    break
                j += 1
            j -= 1
            num[i], num[j] = num[j], num[i]
            num[i+1:] = sorted(num[i+1:])
            return num
    for k in range(0, len(num)/2, 1):
        num[k], num[len(num)-1-k] = num[len(num)-1-k], num[k]
    return num

print nextPermutation(num)

