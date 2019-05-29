arr = [1,3,2,6,5,2,1]
arr2 = [6,5,4,3,2,1]

# array = [1,3,2,6,5]
# bubble_sort(array)
# array = [1,2,3,5,6]

def bubble_sort(array):
    is_sorted = True

    for i in range(0, len(array) - 1):

        if array[i] > array[i + 1]:
            is_sorted = False
            array[i], array[i + 1] = array[i + 1], array[i]

    if is_sorted:
        return array
    else:
        return bubble_sort(array)

print(bubble_sort(arr))
print(bubble_sort(arr2))