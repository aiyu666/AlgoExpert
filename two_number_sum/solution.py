def two_number_sum(array: list, target_sum:int) -> list:
    for x in array:
        cp_arry = array.copy()
        cp_arry.remove(x)
        if cp_arry.count(target_sum-x) == 1:
            return [x, target_sum-x]
    return []