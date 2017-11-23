# insertion sort:

# Algo: 
# 0 move through array
# 1 insert the ith element in sorted position of the ith subarray
# 2 continue until the last element


def insert_sort(arr):
	
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

	print('sorted array: ', arr)


if __name__ == '__main__':

	import random

	arr = [random.randint(0,20) for j in range(10)]

	insert_sort(arr)



