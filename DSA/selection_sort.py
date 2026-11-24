# Selection sort 
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i #starting position
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
               min_index = j
        arr[i], arr[min_index] = arr[min_index],arr[i]
    return arr
arr = [5,2,1,4]
print("Sorted", selection_sort(arr))