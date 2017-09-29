 

def solve(string_input, string_len):
    a = 0
    b = string_len - 1
    str_tmp = ''
    while a <= b:
        left = False
        for i in range(0, string_len-a, 1):
            if string_input[a+i]<string_input[b]:
                left = True
                break
            elif string_input[a+i]>string_input[b]:
                left = False
                break
        if left:
            str_tmp += string_input[a]
            a += 1
        else:
            str_tmp += string_input[b]
            b -= 1
    print str_tmp
    pass
 
def main():
     string_len = 6
     string_input = 'ACDBCB'
     solve(string_input, string_len)
     pass
 
if __name__ == '__main__':
     main()
