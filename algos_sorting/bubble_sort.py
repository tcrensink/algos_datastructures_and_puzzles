#bubble sort: https://practice.geeksforgeeks.org/problems/sort-the-array/0

# BUBBLE SORT FROM MEMORY:
# pairwise comparison of two elements, moving max to right array location
# after first round, a comparison has been made with the largest element and every other (its now sorted at end)

def bubble_sort(arr):

	n = len(arr)

	for i in range(n):

		for j in range(n - i - 1):

			if arr[j] > arr[j+1]:

				arr[j], arr[j+1] = arr[j+1], arr[j]

	print('sorted array: ', arr)
	return arr


























if __name__ == '__main__':

	import random
	arr = [random.randint(0,100) for j in range(10)]
	bubble_sort(arr)






