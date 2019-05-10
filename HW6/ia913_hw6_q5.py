def encode(n):
    lst = []
    count = 0
    temp = n[0]
    for i in range(len(n)):
        if temp == n[i]:
            count +=1
        else:
            lst.append([temp, count])
            temp = n[i]
            count = 1
    lst.append([temp, count])

    return lst


def decode(lst):
    n = ''
    for i in range(len(lst)):
        n += lst[i][0]*lst[i][1]
    return n


n = 'aadccccaa'
print(encode(n))

print(decode(encode(n)))