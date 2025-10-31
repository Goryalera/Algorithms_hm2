def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp
        gap //= 2

if __name__ == "__main__":
    data = [19, 2, 31, 45, 6, 11, 121, 27]
    print("Исходный массив:", data)
    shell_sort(data)
    print("Отсортированный массив:", data)
