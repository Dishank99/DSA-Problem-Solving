# Given an array, rotate the array by one position in clock-wise direction.

def rotate_clockwise_by_1(array):
    if not array: return

    # sace the last ele as it would be placed at oth pos
    last_ele = array[len(array) - 1]
    
    # go from last pos coz this way the ele to be cpoied will be newer unlike if traversed from start pos
    for i in range(len(array)-1, 0, -1):
        array[i] = array[i-1]
    
    array[0] = last_ele

if __name__ == '__main__':
    given_array = [1, 2, 3, 4, 5]
    rotate_clockwise_by_1(given_array)
    print(given_array)