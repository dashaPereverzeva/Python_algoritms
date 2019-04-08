__author__ = 'dashik'

import random

N = 10
li = [random.uniform(0, 50) for _ in range(N)]

def sort_merge(A):
    res = []
    if len(A) == 2:
        if A[0] > A[1]:
            A[0], A[1] = A[1], A[0]
            return A
        else:
            return (A)
    if len(A) < 2:
        return (A)

    else:
        left = sort_merge(A[0: len(A) // 2])
        right = sort_merge(A[len(A) // 2: len(A)])
        while len(left) + len(right) > 0:
            if len(left) == 0:
                for i in right:
                    res.append(i)
                right = []
            elif len(right) == 0:
                for i in left:
                    res.append(i)
                left = []
            elif left[0] > right[0]:
                el = right.pop(0)
                res.append(el)
            elif left[0] <= right[0]:
                el = left.pop(0)
                res.append(el)

        return res


li_sort = sorted(li)

print(li)
print(li_sort)
print(sort_merge(li))
