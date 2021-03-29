def mergesort(data_to_sort):
    global count
    if len(data_to_sort) > 1:
        mid = len(data_to_sort) // 2
        leftarray = data_to_sort[:mid]
        rightarray = data_to_sort[mid:]
        mergesort(leftarray)
        mergesort(rightarray)
        i, j, k = 0, 0, 0
        while i < len(leftarray) and j < len(rightarray):
            if leftarray[i] < rightarray[j]:
                data_to_sort[k] = leftarray[i]
                i += 1
            else:
                data_to_sort[k] = rightarray[j]
                j += 1
            k += 1
            count+=1
        while i < len(leftarray):
            data_to_sort[k] = leftarray[i]
            i += 1
            k += 1
            count+=1
        while j < len(rightarray):
            data_to_sort[k] = rightarray[j]
            j += 1
            k += 1
            count+=1
count = 0
list_to_sort = [2,5,8,11,22,45,54,67,78,89,69,9,7,23,38,40]
print('Original List: ', list_to_sort)
mergesort(list_to_sort)
print('Sorted List: ', list_to_sort)
print("Time complexity:",count)