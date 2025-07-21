def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            #j = j - 1
        arr[j + 1] = key
    return arr


print(insertion_sort([8, 4, 1, 5, 9]))
