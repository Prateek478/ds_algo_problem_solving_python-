def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            # To sort in descending order, change > to < in this line.
            if array[j] > array[j + 1]:
                (array[j], array[j + 1]) = (array[j + 1], array[j])
data = [-2, 45, 0, 11, -9]
bubbleSort(data)
print('bubbleSorted Array in Ascending Order: {}'.format(data))


# Selection sort in Python
def selectionSort(array, size):
    for step in range(size):
        min_idx = step
        for i in range(step + 1, size):
            # To sort in descending order, change > to < in this line.
            if array[i] < array[min_idx]:
                min_idx = i
        (array[step], array[min_idx]) = (array[min_idx], array[step])

data = [-2, 45, 0, 11, -9]
size = len(data)
selectionSort(data, size)
print('selectionSorted Array in Ascending Order: {}'.format(data))

# Insertion sort in Python
def insertionSort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        while j >= 0 and key < array[j]:
            # For descending order, change key<array[j] to key>array[j].
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key
data = [-2, 45, 0, 11, -9]
insertionSort(data)
print('insertionSorted Array in Ascending Order: {}'.format(data))
