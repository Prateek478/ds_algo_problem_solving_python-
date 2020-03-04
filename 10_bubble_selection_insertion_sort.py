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
def selectionSort(a, size):
    for i in range(size-1):
        for j in range(i+1,size):
            if a[i] > a[j]:
                a[i],a[j] = a[j],a[i]
    return a

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
