#recursively sum values in array
#question: does this create a new array 'arr' at each iteration?  What is the time/space complexity of this operation?

def recursive_sum(arr):

	if len(arr) == 0:
		return 0

	else:

		return arr.pop() + recursive_sum(arr)


#other implementation