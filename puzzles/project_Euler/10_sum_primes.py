#Find the sum of all the primes below two million.

#Solution: use a sieve
# create dict with integer keys, value set to True
# iterate through keys. 
#	if key == True:
# 	- add to solution
# 	- mark multiples of prime as False 

#reasonably fast:
def sum_primes(n=2*10**6):

	sum_of_primes = 0
	ints = {el:True for el in range(2,n)}

	for key, value in ints.items():
		if value == True:
			sum_of_primes += key

			#false_keys = 
			for el in range(key**2,n,key):
				ints[el] = False

	return sum_of_primes

# (very slow): int_set contains potential primes.  members are removed as they're ruled out.
# def sum_primes(n=2*10**6):
# 	#primes = []
# 	sum_of_primes = 0
# 	int_set = set.union({2},{j for j in range(3,n,2)})

# 	while len(int_set) > 0:
# 		n0 = min(int_set)
# 	#	primes.append(n0)
# 		sum_of_primes += n0
# 		int_set -= {n0}

# 		#remove all elements that are multiples:		
# 		int_set = {el for el in int_set if el%n0 != 0}	

# 	return sum_of_primes
# 	#return primes