def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1

numbers = [9, 23, 10, 50, 58, 30, 78, 89, 11]

search_element = 58

result_index = linear_search(numbers, search_element)

if result_index != -1:
    print(f"Элемент {search_element} найден на позиции {result_index}.")
else:
    print(f"Элемент {search_element} не найден в списке.")
