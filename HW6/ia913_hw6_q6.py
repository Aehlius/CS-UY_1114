def reverse_to_new_list(lst):
    new_list = []
    for i in range(len(lst)-1, -1, -1):
        new_list.append(lst[i])
    return new_list


def reverse_in_place(lst):
    for i in range(len(lst)):
        lst.insert(-i, lst.pop(0))
    lst.insert(0, lst.pop(-1))


def main():

    lst1 = [1, 2, 3, 4, 5, 6]
    rev_lst1 = reverse_to_new_list(lst1)
    print("After reverse_to_new_list, lst1 is", lst1,
            "and the returned list is", rev_lst1)

    lst2 = [1, 2, 3, 4, 5, 6]
    print("Before reverse_in_place, lst2 is", lst2)
    reverse_in_place(lst2)
    print("After reverse_in_place, lst2 is", lst2)


if __name__ == '__main__':
    main()
