#takes a number and changes base.number

#AS A LIST:
def change_base(n,original_base=10,new_base=2):
	
	(quotient, remainder) = divmod(n,new_base)
	
	if quotient == 0 and quotient == 0:
		return [int(remainder)]
		
	return change_base((n-remainder)/new_base) + [int(remainder)]

change_base(8)


#iterative version
def change_base(n,original_base=10,new_base=2):

	from collections import deque
	n_newbase = deque()

	while True:

		(quotient,remainder) = divmod(n,new_base)	
		if quotient != 0 or remainder != 0:
			
			n = int((n - remainder)/new_base)
			n_newbase.appendleft(remainder)

		else:			
			return n_newbase
		
