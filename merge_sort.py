def merge_sort(array):
    length = len(array)

    if length > 1:
        mid = length//2
        leftArray = array[:mid]
        rightArray = array[mid:]

        merge_sort(leftArray)
        merge_sort(rightArray)
        merge(array, leftArray, rightArray)


def merge(array, leftArray, rightArray):
    i = j = k = 0
    while i < len(leftArray) and j < len(rightArray):
        if leftArray[i] < rightArray[j]:
            array[k] = leftArray[i]
            i += 1

        else:
            array[k] = rightArray[j]
            j += 1
        k += 1

    while(i < len(leftArray)):
        array[k] = leftArray[i]
        i += 1
        k += 1

    while(j < len(rightArray)):
        array[k] = rightArray[j]
        j += 1
        k += 1


if __name__ == "__main__":
    a = [11, 1, 4, 27, 36, 15, -1, 3, 1]
    merge_sort(a)
    print(a)
