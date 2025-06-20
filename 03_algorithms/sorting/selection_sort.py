def selection_sort(unsorted_list):
    n = len(unsorted_list)

    for i in range(n):
        min_index = i  # Start by assuming the current index has the smallest value

        # Find the index of the smallest value in the remaining list
        for j in range(i + 1, n):
            if unsorted_list[j] < unsorted_list[min_index]:
                min_index = j

        # Swap the values using a temporary variable (temp)
        temp = unsorted_list[i]
        unsorted_list[i] = unsorted_list[min_index]
        unsorted_list[min_index] = temp

    return unsorted_list


numbers = [29, 10, 14, 37, 1, 4]
print(numbers)
sorted_numbers = selection_sort(numbers)
print("Sorted list:", sorted_numbers)
