def insertion_sort(arr):
	for i in range(1, len(arr)):
    	key = arr[i]  
    	j = i - 1  
    	while j >= 0 and arr[j] > key:
        	arr[j + 1] = arr[j] 
        	j -= 1  
    	arr[j + 1] = key
	return arr
array = [7,0,3,5,6]
print("Исходный массив:", array)
sorted_array = insertion_sort(array)
print("Отсортированный массив:", sorted_array)
