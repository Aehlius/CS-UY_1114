def create_prefix_lists(lst):
    final_lst = []
    for i in range(len(lst)):
        temp_lst = lst[0:i]
        final_lst.append(temp_lst)
    final_lst.append(lst)
    return final_lst


lst = [2, 4, 6, 8, 10]
print(create_prefix_lists(lst))