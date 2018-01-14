#finds all prime factors of n:

def get_factors(n):

	factors = []
	f = 2

	while n > 1:
		while divmod(n,f)[1] == 0:

			factors.append(f)
			n /= f
		f += 1

	return factors


if __name__ == "__main__":

	import random
	n = random.randint(1,1000000)

	print(get_factors(n))

