#Insertion sort
n= int(input('Enter length of array'))
a = list(map(int,input('Enter elements').strip().split()))[:n]
def insertionSort(a):
    cnt=0
    for i in range(1, len(a)):
        key = a[i]
        j = i-1
        while j >=0 and key < a[j] :
            a[j+1] = a[j]
            j -= 1
            cnt=cnt+1
        a[j+1] = key
    print("complexity of insertion sort is ",cnt)
insertionSort(a)
print("Sorted array")
for i in range(len(a)):
    print("%d" % a[i]),