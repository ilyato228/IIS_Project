from array import *


def left_join(l1, l2):
    res = []
    ar1 = array('i', l1)
    ar2 = array('i', l2)
    for i in ar1:
        if i not in ar2:
            res.append(i)
    res = array('i', res)
    return res
