from cgitb import reset


def solution(array: list, target_sum):
    for x in array:
        cp_arry = array.copy()
        cp_arry.remove(x)
        if cp_arry.count(target_sum-x) == 1:
            return [x, target_sum-x]
    return []