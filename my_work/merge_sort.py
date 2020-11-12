
# split array into smaller arrays by half until they are individual numbers

# base case: when list length is 1 (already sorted)

# https://stackabuse.com/merge-sort-in-python/

import sys

def merge_sort(A):
	merge_sort2(A, 0, len(A)-1)
	
def merge_sort2(A, first, last):
	if first < last:
		middle = (first + last)//2
		merge_sort2(A, first, middle)
		merge_sort2(A, middle+1, last)
		return merge(A, first, middle, last)
		
def merge(A, first, middle, last):
	L = A[first:middle+1]
	R = A[middle+1:last+1]
	L.append(sys.maxsize)
	R.append(sys.maxsize)
	i = j = 0
	
	for k in range (first, last+1):
		if L[i] <= R[j]:
			A[k] = L[i]
			i += 1
		else:
			A[k] = R[j]
			j += 1


mouse = [3, 6, 7, 4, 5, 3, 2, 1]
A = [5,9,1,2,4,8,6,3,7]
print(mouse)
merge_sort(mouse)
print(mouse)