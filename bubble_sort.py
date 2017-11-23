#bubble sort: https://practice.geeksforgeeks.org/problems/sort-the-array/0


# move sequentially through an array, swapping adjacent entries if they're out of order.  Sweep through until array is sorted.


def bubble_sort(arr):

	sorted = False
	while sorted == False:
		
		sorted = True
		
		for j in range(len(arr)-1):

			if arr[j] > arr[j+1]:
				
				sorted = False
				arr[j], arr[j+1] = arr[j+1], arr[j]

	print('sorted array:', arr)
	return arr


# POSTED SOLUTION.  Can truncate inner loop by 'i' since they are sorted at the end.
def bubbleSort(arr):
	n = len(arr)
 
	# Traverse through all array elements
	for i in range(n):
 
		# Last i elements are already in place
		for j in range(0, n-i-1):
 
			# traverse the array from 0 to n-i-1
			# Swap if the element found is greater
			# than the next element
			if arr[j] > arr[j+1] :
				arr[j], arr[j+1] = arr[j+1], arr[j]

	print('sorted array:', arr)
	return arr


if __name__ == '__main__':

	import random
	arr = [random.randint(0,100) for j in range(10)]
	bubble_sort(arr)






