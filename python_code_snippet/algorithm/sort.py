# coding=utf-8
def bubble_sort(lst):
    lst_len = len(lst)
    if lst_len < 2 :
        return lst

    for i in range(lst_len):
        for j in range(1, lst_len-i):
            if lst[j-1] > lst[j]:
                lst[j - 1], lst[j] = lst[j], lst[j - 1]
    return lst


lst = [2,3,4,8,6,5,1,7]
print sorted(lst)
print bubble_sort(lst)
