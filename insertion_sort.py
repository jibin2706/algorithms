def insertion_sort(a):
    for i in range(1, len(a)):
        current_value = a[i]
        position = i
        while position > 0 and current_value < a[position-1]:
            a[position] = a[position-1]
            position -= 1
        a[position] = current_value


if __name__ == "__main__":
    a = [11, 1, 4, 27, 36, 15, -1, 3, 1]

    insertion_sort(a)
    print(a)
