# implement recursive call quicksort algo:
# https://github.com/TheAlgorithms/Python/blob/master/sorts/quick_sort.py
# https://stackoverflow.com/questions/18262306/quicksort-with-python

# quicksort algo:
# 1) choose a "pivot" value from the array
# 2) move all elements less than pivot to left, more to right
# 3) treat sub arrays the same: choose pivot, and sort leq to left, greater to right of pivot(s)
# 4) stop when you get to array length of 1

#it has been noted that this is not an "in place" solution and requires more memory:
def quick_sort(arr):
	
	if len(arr) > 1:

		pivot = arr[0]
		lower = [el for el in arr[1:] if el <= pivot]
		higher = [el for el in arr[1:] if el > pivot]

		return quick_sort(lower) + [pivot] + quick_sort(higher)

	else:

		return arr


# in place solution...
#def quick_sort(arr):





if __name__ == "__main__":

	import random
	arr = [random.randint(0,15) for el in range(10)]

	print('unsorted array: ', arr)
	print('sorted array: ', quick_sort(arr))