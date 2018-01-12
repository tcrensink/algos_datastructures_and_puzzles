# returns time of execution as a function of (linearly increasing) values of n.
import numpy as np
import time
import random
import matplotlib.pyplot as plt

def return_times(sort_algorithm, n_values=np.linspace(100,8000,20).astype('int')):

	start_time	= []
	end_time	= []
	#array creation
	for (j,n) in enumerate(n_values):
		arr = [random.randint(0,5*n) for value in range(n)]
		start_time.append(time.time())
		sort_algorithm(arr)
		end_time.append(time.time())

	run_times = [t_end - t_start for (t_start,t_end) in zip(start_time, end_time)]
	return run_times
	
def plot_sort_time(n_values,run_times):

	plt.plot(n_values,run_times)
	plt.show()