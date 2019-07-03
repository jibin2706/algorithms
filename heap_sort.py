# Time complexity: O(nlogn)
# Space complexity: O(1)


def buildMaxHeap(array):
    i = len(array)//2 - 1

    # passing root node and applying heapify
    while i >= 0:
        heapify(array, i, len(array))
        i -= 1


def heapify(array: list, root, max):
    # max is length of the heap

    largest = root
    left = root * 2 + 1
    right = left + 1

    # check if the index exist and greater than the root
    if left < max and array[left] > array[largest]:
        largest = left
    if right < max and array[right] > array[largest]:
        largest = right

    # if the nodes are correctly placed
    if root == largest:
        return

    # else swap the numbers
    array[largest], array[root] = array[root], array[largest]
    heapify(array, largest, max)


def heap_sort(array):
    n = len(array)

    # extract root element which will be largest
    for i in range(n-1, -1, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, 0, i)


if __name__ == "__main__":
    arr = [11, 1, 4, 27, 36, 15, -1, 3, 1]
    # building max heap
    buildMaxHeap(arr)

    # applying heap sort
    heap_sort(arr)
    print(arr)
