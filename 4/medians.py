__author__ = 'Sergei.Ivanov'

from bisect import bisect
with open("input.txt") as f, open("output.txt", "w") as g:
    line = f.readlines()[1]
    d = map(int, line.split())
    if not d:
        S = 0
    elif len(d) == 1:
        S = d[0]
    else:
        if d[0] < d[1]:
            arr = d[:2]
            S = 2*d[0]
        else:
            arr = [d[1], d[0]]
            S = d[0] + d[1]
        for el in d[2:]:
            idx = bisect(arr, el)
            arr.insert(idx, el)
            if not len(arr)%2:
                prev_idx = len(arr)//2 - 1
            else:
                prev_idx = (len(arr) + 1)//2 - 1
            median = arr[prev_idx]
            print median
            S += median
    g.write(str(S))
#
# if not d:
#     S = 0
# elif len(d) == 1:
#     S = d[0]
# else:
#     arr, S = first_two_medians(d[:2])
#     # print arr, S
#     for el in d[2:]:
#         idx2 = insert_el(el, arr)
#         arr.insert(idx, el)
#
#         # insert_el2(el, arr)
#         prev_idx = median_idx(arr)
#         median = arr[prev_idx]
#         # print arr, prev_idx, median
#         S += median
#
# print S