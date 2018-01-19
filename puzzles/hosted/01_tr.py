def Solution(M):

	N = len(M)
	for j1 in range(N + 1):
		for j2 in range(j1):
			j = j2
			k = N + (j2 - j1)
			# print('({}, {}) '.format(j, k), end='')
			print('{:2d} '.format(M[j][k]), end='')
		print('')
		
	for j1 in range(N):
		for j2 in range(N - j1 - 1):	
			j = j1 + j2 + 1
			k = j2
			# print('({}, {}) '.format(j1, j2), end='')
			# print('({}, {}) '.format(j, k), end='')
			print('{:2d} '.format(M[j][k]), end='')
		print('')
		
if __name__ == '__main__':

	import numpy as np
	#import pprint
	N = 5
	M = np.random.randint(100, size=(N, N)).tolist()

	print('M:')
	for row in M:
		print(row)
	print('\nSolution:')
	Solution(M)
