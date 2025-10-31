#include <iostream>
#include <vector>

int interpolationSearch(const std::vector<int>& arr, int x) {
    int low = 0;
    int high = arr.size() - 1;

    while (low <= high && x >= arr[low] && x <= arr[high]) {
        if (low == high) {
            if (arr[low] == x) return low;
            return -1;
        }

        // Формула интерполяционного поиска
        int pos = low + ((double)(high - low) / (arr[high] - arr[low])) * (x - arr[low]);

        if (arr[pos] == x)
            return pos;

        if (arr[pos] < x)
            low = pos + 1;
        else
            high = pos - 1;
    }

    return -1; // элемент не найден
}

int main() {
    std::vector<int> arr = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100};
    int x = 70;
    int index = interpolationSearch(arr, x);

    if (index != -1)
        std::cout << "Элемент " << x << " найден на позиции " << index << std::endl;
    else
        std::cout << "Элемент " << x << " не найден в массиве." << std::endl;

    return 0;
}
