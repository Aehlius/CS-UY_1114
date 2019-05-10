

def add_list(lst1, lst2):
    lst3 = []
    for i in range(len(lst1)):
        lst3.append(int(lst1[i])+int(lst2[i]))
    return lst3


def main():

    lst1 = []
    lst2 = []
    var1 = 0
    var2 = 0
    print('Please enter a number for first list, followed by done: ')
    while var1 != 'done':
        var1 = input()
        lst1.append(var1)

    print('Please enter a number for second list, followed by done: ')
    while var2 != 'done':
        var2 = input()
        lst2.append(var2)

    del lst1[-1]
    del lst2[-1]

    if len(lst1) != len(lst2):
        print('Lists are different lengths.')
    else:
        lst3 = add_list(lst1, lst2)
        for i in range(len(lst3)):
            print(lst3[i])


if __name__=='__main__':
    main()


