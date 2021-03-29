#Selection sort
cnt = 0
n= int(input('Enter length of array'))
A = list(map(int,input('Enter elements').strip().split()))[:n]
for i in range(len(A)):
    min_idx = i
    for j in range(i + 1, len(A)):
        cnt = cnt + 1
        if A[min_idx] > A[j]:
            min_idx = j
    A[i], A[min_idx] = A[min_idx], A[i]
print("Sorted array")
for i in range(len(A)):
    print("%d" % A[i])
print('Complexity of selection sort is',cnt)
