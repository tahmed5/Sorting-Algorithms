# Quick Sort = Think of Pivot
# Pivot Conditions
#  1. Corret position in final, sorted array
#  2. Items to the left are smaller than the pivot
#  3. Items to the right are larger than the pivot

#2 6 5 0 8 7 1 3
# Pivot = 3
# Move to the end
# ItemFromLeft= First item from left larger than pivot
# ItemFromRight = First items that is smaller than pivot
# ItemFromLeft = 6,
# ItemFromRight = 1,
# Swap ItemFromLeft with ItemFromRight
# 2 1 5 0 8 7 6 3
# ItemFromLeft = 5
# ItemFromRight = 0
#Swap
# 2 1 0 5 8 7 6 3
# ItemFromLeft index > ItemFromRight so finished with pivot 3.
#Swap ItemFromLeft with pivot.
# 2 1 0 3 8 7 6 5

#Larger Partition.
# 8 7 6 5
#Pivot = 7
# 8 5 6 7
# ItemFromLeft = 8
# ItemFromRight = 6
#Swap
# 6 5 8 7
# ItemFromLeft = 8
# ItemFromRight = 5
# ItemFromLeft index > ItemFromRight so finished with pivot 7
#Swap ItemFromLeft with pivot
# 6 5 7 8

#How to choose pivot
# Divide the array in half to split work evenly
#
# 1 way to do this is the median of 3 method
# where you take the first, middle and last item in your list and
# pick the median value as your pivot

#QuickSort is a recursive method
#Divide and Conquer algorithm
#Very efficient for large data sets.
#BIG O
#BEST - O(nlog(n))
#AVERAGE - O(nlog(n))
#WORST - O(n^2)
#SPACE - O(log(n))
#Performance largely deponds on Pivot


def quick_sort_define(A):
    quick_sort(A, 0, len(A) -1)

def quick_sort(A, low, hi):
    if low < hi:
        p = partition(A, low, hi)
        quick_sort(A, low, p-1)
        quick_sort(A, p+1, hi)

def get_pivot(A, low, hi):
    mid = (hi + low) // 2
    pivot = hi
    if A[low] < A[mid]:
        if A[mid] < A[hi]:
            pivot = mid
    elif A[low] < A[hi]:
        pivot = low

    return pivot

def partition(A, low, hi):
    pivotIndex = get_pivot(A,low,hi)
    pivotValue = A[pivotIndex]
    A[pivotIndex], A[low] = A[low], A[pivotIndex]
    border = low
    for i in range (low, hi +1):
        if A[i] < pivotValue:
            border += 1
            A[i], A[border] = A[border], A[i] 
    A[low], A[border] = A[border],A[low]

    return border


A = [2,6,5,0,8,7,1,3]
quick_sort_define(A)
print(A)
