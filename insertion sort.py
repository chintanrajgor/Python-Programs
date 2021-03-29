#INSERTION SORT
def insertionSort(arr):
    count=0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            count=count+1
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    print("count is", count)
n = int(input("Enter number of elements : "))
arr = list(map(int, input("\nEnter the numbers : ").strip().split()))[:n]
insertionSort(arr)
print("Sorted array is:")
for i in range(len(arr)):
    print("%d" % arr[i])
