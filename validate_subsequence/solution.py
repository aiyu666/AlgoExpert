def isValidSubsequence(array: list, sequence:list) -> bool:
    min_index = 0
    for x in sequence:
        if x not in array:
            return False
        index = array.index(x)
        if index < min_index:
            return False
        min_index = index
        array[index] = None
    return True