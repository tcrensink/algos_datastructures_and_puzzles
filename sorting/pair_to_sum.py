#problem: http://www.techiedelight.com/find-pair-with-given-sum-array/

#find pairs of numbers in an array that will sum to a specific number, e.g.:
#arr = [8,7,2,5,3,1]
#sum = 10
#output: pair found at index 0 and 2 (8 + 2)
# OR     pair found at index 1 and 4 (7 + 3)

# BRUTE FORCE: n^2 time complexity... can be done faster.  Looking for one pair?
def return_pair(arr,sum):

	for (j,n1) in enumerate(arr):

		for (k,n2) in enumerate(arr[j:]):

			if n1 + n2 = sum

			print(pair found at index ', j, 'and ', k, '(',n1,' + ',n2,')')
			break


	else print('no pairs found.')



# sort array first? nlogn then search for other value (10 - n1), store in hash table
