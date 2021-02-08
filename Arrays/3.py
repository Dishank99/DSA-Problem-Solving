# Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.

def sort_array(array):
    if not array: return

    count_0, count_1, count_2 = 0, 0, 0

    for element in array:
        if element == 0: count_0 += 1 
        if element == 1: count_1 += 1 
        if element == 2: count_2 += 1

    # updating array in place as array are mutable
    i = 0
    while count_0 > 0:
        array[i] = 0
        count_0-=1
        i+=1
    while count_1 > 0:
        array[i] = 1
        count_1-=1
        i+=1
    while count_2 > 0:
        array[i] = 2
        count_2-=1
        i+=1

if __name__ == '__main__':
    given_array = [0,1,1,2,1,2,0,2,1,0]
    sort_array(given_array)
    print(given_array)
