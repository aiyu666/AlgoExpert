def sorted_squared_array(array):
    array = list(map(abs, array))
    array.sort()
    result = [x**2 for x in array]
    return result
