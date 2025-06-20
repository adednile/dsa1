def bubble_sort(unsorted_list):
    number_of_elements = len(unsorted_list)

    # Repeat the process for each element in the list
    for outer_loop in range(number_of_elements):

        # Go through the list up to the last unsorted element
        for inner_loop in range(0, number_of_elements - 1 - outer_loop):

            # If the current item is bigger than the next one, swap them
            if unsorted_list[inner_loop] > unsorted_list[inner_loop + 1]:

                # Swap using a temp variable
                temp = unsorted_list[inner_loop]
                unsorted_list[inner_loop] = unsorted_list[inner_loop + 1]
                unsorted_list[inner_loop + 1] = temp

    return unsorted_list

#
numbers = [29, 10, 14, 37, 1]
print(numbers)
sorted_numbers = bubble_sort(numbers)
print("Sorted list:", sorted_numbers)
