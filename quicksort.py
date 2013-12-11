import random

def quicksort(in_array):
    if len(in_array) <= 1:
        return in_array
    else:
        pivot = random.choice(range(len(in_array)-1))
        pivot_val = in_array[pivot]
        in_array.pop(pivot)
        lower = []
        higher = []
        for element in in_array:
            if element < pivot_val:
                lower.append(element)
            else:
                higher.append(element)

        return quicksort(lower) + [pivot_val] + quicksort(higher)

def quicksort_in_place(in_array):
    if len(in_array) <= 1:
        return in_array
    else:
        pivot = random.choice(range(len(in_array)-1))
        pivot_val = in_array[pivot]
        i = 0
        j = len(in_array) - 1 
        if in_array[i] > pivot_val and in_array[j] < pivot_val:
            #swap
            continue
        if in_array[i] < pivot_val:
            i += 1
        if in_array[j] > pivot_val:
            j -= 1
        

print quicksort([5,7,2,10,35,7,2,11])