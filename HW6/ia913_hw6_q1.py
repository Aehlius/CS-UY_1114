def max_abs_val(lst):
    high = 0
    for i in range(len(lst)):
        if high < abs(lst[i]):
            high = abs(lst[i])

    return high


lst = [-19, -3, 20, -1, 0, -25]
print(max_abs_val(lst))

