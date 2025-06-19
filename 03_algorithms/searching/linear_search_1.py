
def get_values(items, key):
    for item in items:
        if item == key:
            # print(f" {item} found")
            return item
    return -1

random_values = [5, -1, 44, 7, 90, 12, ]
print(random_values)
key = int(input("Enter number to search : "))

# print(get_values(random_values, key))

result = get_values(random_values, key)
print(result)


