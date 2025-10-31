def bubble_sort(arr): 
    n = len(arr)      
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = [70, 50,40,30,55,44,20]  
print("Исходный массив:", arr)
bubble_sort(arr)  
print("Отсортированный массив:", arr)
