def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr

arr = list(map(int, input("Enter elements separated by space: ").split()))
sorted_arr = insertion_sort(arr)
print("Sorted array:", sorted_arr)
