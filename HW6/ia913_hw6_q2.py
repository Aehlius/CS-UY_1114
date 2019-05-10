def find_all(lst, val):
    index = []
    for i in range(len(lst)):
        if val == lst[i]:
            index.append(i)
    return index


ls = ['a', 'b', '10', 'bab', 'a']
print(find_all(ls, 'a'))
