def merge_sort_descending(data):
    if len(data) > 1:
        mid = len(data) // 2
        left_half = data[:mid]
        right_half = data[mid:]
        merge_sort_descending(left_half)
        merge_sort_descending(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] > right_half[j]:
                data[k] = left_half[i]
                i += 1
            else:
                data[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            data[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            data[k] = right_half[j]
            j += 1
            k += 1

data = [3, 1, 4, 1, 5, 9, 2, 6, 5]
merge_sort_descending(data)
print("Sorted array in descending order:", data)
