# Find the Union and Intersection of the two sorted arrays.

# approach 1 is converting both array to sets and find union and intersection => tc = n, sc = n approach

def find_intersection(array1, array2):

    # base cases
    if not array1 or not array2:
        return []

    i = j = 0

    intersection_array = []

    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]: # since arrays are sorted to move towards finding common ele
            i+=1
        elif array2[j] < array1[i]:
            j+=1
        else: # if common ele is found
            intersection_array.append(array1[i])
            i+=1
            j+=1

    return intersection_array

def find_union(array1, array2):

    # base cases
    if array1 and not array2: 
        return array1
    if array2 and not array1:
        return array2
    if not array1 and not array2: 
        return []

    i = j = 0

    union_array = []

    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]: # since arrays are sorted to move towards finding common ele
            union_array.append(array1[i])
            i+=1
        elif array2[j] < array1[i]:
            union_array.append(array2[j])
            j+=1
        else: # if common ele is found
            union_array.append(array1[i])
            i+=1
            j+=1
    
    while i < len(array1):
        union_array.append(array1[i])
        i+=1
    
    while j < len(array2):
        union_array.append(array2[j])
        j+=1

    return union_array
        

if __name__ == '__main__':
    array1 = [1, 2, 3, 4, 5, 6]
    array2 = [1, 2, 3]

    intersection = find_intersection(array1, array2)
    union = find_union(array1, array2)

    print(union)
