# insertion sort:

# Algo: 
# 0 move to next unsorted element in array, the key
# 1 scan through sorted subarray (to the left); find the position it belongs
# 2 move all larger sorted elements to the right by one step
# 3 insert the key


def insertion_sort(arr):
	
	l = len(arr)

	#move through array
	for j in range(1, l ):

		key = arr[j]

		#sort sub-array:
		k = j-1
		while (arr[k] > key) and (0 <= k):

			arr[k+1] = arr[k]
			k -= 1

		arr[k+1] = key

	return arr


if __name__ == '__main__':

	import random
	arr = [random.randint(0,12) for j in range(8)]

	print('original array: ', arr)
	print('sorted array: ', insertion_sort(arr))



