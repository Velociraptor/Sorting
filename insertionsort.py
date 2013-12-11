def insertion(in_array):
    sorted_array = [in_array[0]]
    for element in in_array[1:]:
        # insert into sorted array
        start_len = len(sorted_array)
        for j in range(start_len):
            if element < sorted_array[j]:
                sorted_array = sorted_array[:j] + [element] + sorted_array[j:]
                break
        if len(sorted_array) == start_len:
            sorted_array += [element]
    return sorted_array

print insertion([3,10,2,5,14,12,63,6,3,63])

def insertion_inplace(in_array):
    for i in range(len(in_array[1:])):
        for j in range(i):
            if in_array[i-j] < in_array[i-j-1]:
                in_array[i-j-1], in_array[i-j] = in_array[i-j], in_array[i-j-1]
                print in_array
            else:
                break
    return in_array


print insertion_inplace([3,10,2,5,14,12,63,6,3,63])



    #for i in range(len(in_array)):
