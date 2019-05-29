arr = [1,3,2,6,5,2,1]

# array = [1,3,2,6,5]
# bubble_sort(array)
# array = [1,2,3,5,6]

def bubble_sort(array):
    i = 0
    is_sorted = True

    while i < len(array) - 1:
        curr_val = array[i]
        next_index = i + 1
        next_val = array[next_index]

        if curr_val > next_val:
            is_sorted = False
            array[next_index] = curr_val
            array[i] = next_val

        i += 1

    if is_sorted:
        return array
    else:
        return bubble_sort(array)

print(bubble_sort(arr))