#algo:

# 1 array is divided into two parts; sorted sub array (left) and unsorted (right)
# 2 scan through unsorted array to find next minimum (or max) element; swap leftmost unsorted element with next sorted element
# 3 repeat until all elements are sorted.are


def selection_sort(arr):

	n = len(arr)

	for j in range(n - 1):

		ind_of_min = j

		for k in range(j + 1, n):

			if arr[k] < arr[ind_of_min]:

				ind_of_min = k

		arr[j], arr[ind_of_min] = arr[ind_of_min], arr[j]

	return arr


if __name__ == "__main__":

	import random
	arr = [random.randint(0,100) for j in range(10)]
	print('original array: ', arr)
	print('sorted array: ', selection_sort(arr))