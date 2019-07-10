# k is range between 1 and largest no
# Time complexity: O(n+k)
# Space complexity: O(k)


def count_sort(array):
    largest_no = max(array)

    count_list = [0]*(largest_no+1)
    result_array = [None]*len(array)

    for i in array:
        count_list[i] += 1

    # for zero based indexing
    count_list[0] = count_list[0] - 1

    for i in range(1, len(count_list)):
        count_list[i] += count_list[i-1]

    # inserting the element into the array and decrementing the count
    for x in array:
        result_array[count_list[x]] = x
        count_list[x] -= 1

    return result_array


if __name__ == "__main__":
    a = [11, 1, 4, 27, 36, 15, 3, 1]
    b = count_sort(a)
    print(b)
