# mergesort algorithm:

# 1) write a merge_sort function that recursively bisects left and right indices until they reach length 1
# 2) write a recursive merge_sort function that updates indices after appending to a solution array

def merge_sort(arr):

	#split initial array into left, right parts:
	if len(arr) <= 1:

		return arr

	i0 				= int(len(arr)/2)
	arr_left 		= merge_sort(arr[:i0])
	arr_right 		= merge_sort(arr[i0:])
	return merge(arr_left, arr_right)


def merge(left_arr, right_arr):

	sorted_arr = []
	#index of left, right arrays
	j = 0
	k = 0

	#if either array is exhausted, the other array may simply be appended to the solution array:
	while (j < len(left_arr)) and (k < len(right_arr)):
		
		#append lesser (leftmost) element to solution array:
		if left_arr[j] < right_arr[k]:
			
			sorted_arr.append(left_arr[j])
			j += 1
		
		else:
			sorted_arr.append(right_arr[k])
			k += 1

	sorted_arr += left_arr[j:]
	sorted_arr += right_arr[k:]

	return sorted_arr


#demonstrate algo if run as main python script:
if __name__ == '__main__':

	import random
	arr = [random.randint(0,16) for j in range(8)]

	print('original array: ', arr)
	print('sorted array: ', merge_sort(arr))
