def quickSort(data_to_sort, first, last):
    if first < last:
        pivotindex = partition(data_to_sort, first, last)
        quickSort(data_to_sort, first, pivotindex - 1)
        quickSort(data_to_sort, pivotindex + 1, last)
def partition(values, first, last):
    global count
    pivotvalue = values[first]
    lower = first + 1
    upper = last
    done = False
    while not done:
        count+=1
        while lower <= upper and values[lower] <= pivotvalue:
            lower += 1
        while values[upper] >= pivotvalue and upper >= lower:
            upper -= 1
        count+=1
        if upper < lower:
            done = True
        else:
            temp = values[lower]
            values[lower] = values[upper]
            values[upper] = temp
        count+=1
    temp = values[first]
    values[first] = values[upper]
    values[upper] = temp
    count+=1
    return upper
count = 0
list = [3,9,11,12,13,23,34,45,67,89,98,87,65,43,32,69]
print('Original List: ', list)
quickSort(list, 0, len(list) - 1)
print('Sorted List: ', list)
print("Time complexity:",count)