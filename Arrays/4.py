# Move all negative numbers to beginning and positive to end with constant extra space

#n2 approach
# def move_negative_numbers(array):
#     if not array: return

#     negative_pointer = 0
#     positive_pointer = len(array)-1

#     i=0
#     while i < positive_pointer:
#         if array[i] > 0:
#             if array[positive_pointer] < 0:
#                 array[i],array[positive_pointer] = array[positive_pointer], array[i]
#                 i+=1
#             else:
#                 while array[positive_pointer] > 0 and positive_pointer > 0:
#                     positive_pointer-=1
#         else:
#             i+=1
#         print(given_array)

# n1 approach
def move_negative_numbers(array):
    if not array: return

    start = 0
    end = len(array) - 1

    while start < end:
        if array[start] < 0:
            start+=1
        if array[end] > 0:
            end-=1
        if array[start] > 0:
            if array[end] < 0:
                array[start], array[end] = array[end], array[start]
        
        print(given_array)


if __name__ == '__main__':
    array1 = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
    array2 = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
    array3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    given_array = array2
    move_negative_numbers(given_array)
    print(given_array)