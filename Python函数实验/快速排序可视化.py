def quickSort(arr, left=None, right=None):
    left = 0 if not isinstance(left, (int, float)) else left
    right = len(arr) - 1 if not isinstance(right, (int, float)) else right
    if left < right:
        partitionIndex = partition(arr, left, right)
        print(partitionIndex)
        quickSort(arr, left, partitionIndex - 1)
        quickSort(arr, partitionIndex + 1, right)
    print(arr)
    return arr


def partition(arr, left, right):
    pivot = left
    index = pivot + 1
    i = index
    while i <= right:
        if arr[i] < arr[pivot]:
            swap(arr, i, index)
            index += 1
        i += 1
    swap(arr, pivot, index - 1)
    return index - 1


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


if __name__ == '__main__':
    nums = [1, 2, 33, 4, 56, 7, 4, 67, 8, 53, 453, 45, 67, 34, 7, 1, 6, 24, 766, 3]
    quickSort(nums)
