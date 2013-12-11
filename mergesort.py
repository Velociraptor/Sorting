def merge(array1, array2):
    merged = []
    i = 0
    j = 0
    while i < len(array1) and j < len(array2):
        i_val = array1[i]
        j_val = array2[j]
        if (i_val < j_val) or (i_val == j_val):
            merged.append(i_val)
            i += 1
        elif j_val < i_val:
            merged.append(j_val)
            j += 1
    if i < len(array1):
        merged += array1[i:]
    elif j < len(array2):
        merged += array2[j:]
    return merged

# print merge([5,10,13,14],[2,4,12,14])

def mergesort(in_array):
    if len(in_array) <= 1:
        return in_array
    else:
        k = len(in_array)/2
        early = in_array[:k]
        late = in_array[k:]
        return merge(mergesort(early),mergesort(late))

print mergesort([3,10,2,5,14,12,63,6,3,63])