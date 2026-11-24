def merge_sort(arr):
    if len(arr) <=1:
      return arr
#  Divide and conquer
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
# Recursion way to divide an array till single element
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left,right)
def merge(left,right):
    result = []
    i = 0
    j = 0
    while i< len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # Append any remaining elements from either list
    result.extend(left[i:])
    result.extend(right[j:])
    return result