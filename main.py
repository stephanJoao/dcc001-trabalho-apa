import numpy as np
import matplotlib.pyplot as plt
import time
import pandas as pd

import sys
sys.setrecursionlimit(10**6)

# criação da lista embaralhada
def create_shuffled_list(size=10, shuffle_rate=0):
	arr = list(range(size))
	n_swaps = int(size * shuffle_rate)
	# print(n_swaps)
	# for i in range(n_swaps):
	# 	a = np.random.randint(0, size)
	# 	b = np.random.randint(0, size)
	# 	arr[a], arr[b] = arr[b], arr[a]
	# return arr
	swaps = np.random.randint(0, size, n_swaps*2)
	for i in range(0, n_swaps*2, 2):
		arr[swaps[i]], arr[swaps[i+1]] = arr[swaps[i+1]], arr[swaps[i]]
	return arr


# métodos de escolha do pivô

# primeiro elemento
def first_pos(arr, lo, hi):
	return lo

# elemento do meio
def middle_pos(arr, lo, hi):
	# print((hi - lo) // 2 + lo)
	return (hi - lo) // 2 + lo

# mediana (de três)
def median(arr, lo, hi):	
	mid = (hi - lo) // 2 + lo 
	if arr[lo] > arr[mid]:
		arr[lo], arr[mid] = arr[mid], arr[lo]
	if arr[mid] > arr[hi]:
		arr[mid], arr[hi] = arr[hi], arr[mid]
	if arr[lo] > arr[mid]:
		arr[lo], arr[mid] = arr[mid], arr[lo]
	return mid

# média
def mean(arr, lo, hi):
	arr_mean = np.mean(arr[lo:hi + 1])
	# return the closest value to the mean
	return np.argmin(np.abs(arr[lo:hi + 1] - arr_mean)) + lo

# elemento aleatório
def random_pos(arr, lo, hi):
	return np.random.randint(lo, hi + 1)

# procedimento AchaPivo
def AchaPivo(arr, lo, hi):
	pos = lo + 1
	while pos <= hi:
		if arr[pos] >= arr[pos-1]:
			pos += 1
		else:
			return pos
	return hi

# método de partição (Hoare's)
def partition(arr, lo, hi, find_pivot):
	# choose pivot
	pivot_value = arr[find_pivot(arr, lo, hi)]
	# print('pivot value: ', pivot_value)

	# left index
	i = lo - 1

	# right index
	j = hi + 1

	while True:
		# move left index to the right while the value is less than the pivot
		i += 1
		while arr[i] < pivot_value:
			i += 1

		# move right index to the left while the value is greater than the pivot
		j -= 1
		while arr[j] > pivot_value:
			j -= 1

		# if the indexes have crossed, return the right index
		if i >= j:
			return j
		
		# swap the values
		arr[i], arr[j] = arr[j], arr[i]

# quicksort
def quicksort(arr, lo, hi, find_pivot):
	if lo >= 0 and hi >= 0 and lo < hi:	
		print('toma tempo????')
		p = partition(arr, lo, hi, find_pivot)	
		quicksort(arr, lo, p, find_pivot)
		quicksort(arr, p + 1, hi, find_pivot)

# main
if __name__ == "__main__":
	sizes = [10**i for i in range(1, 9)]
	shuffle_rates = [0.05, 0.25, 0.45]
	pivot_functions = [middle_pos, median, random_pos, mean, first_pos]
	n_experiments = 10
	
	'''results = []
	
	for size in sizes:
		for shuffle_rate in shuffle_rates:
			for pivot_function in pivot_functions:
				results = []
				for i in range(n_experiments):
					l = create_shuffled_list(size=size, shuffle_rate=shuffle_rate)
					start = time.process_time()
					quicksort(l, 0, size - 1, pivot_function)
					end = time.process_time()
					print([size, shuffle_rate, pivot_function.__name__, i, end - start])
					results.append([size, shuffle_rate, pivot_function.__name__, i, end - start])
				results = pd.DataFrame(results, columns=['size', 'shuffle_rate', 'pivot_function', 'experiment', 'time'])
				name = f'results/results_{size}_{shuffle_rate}_{pivot_function.__name__}.csv'
				results.to_csv(name, index=False, sep=';')''' # experiments

	# append all results to one file
	results = pd.DataFrame()
	for size in sizes:
		for shuffle_rate in shuffle_rates:
			for pivot_function in pivot_functions:
				name = f'results/results_{size}_{shuffle_rate}_{pivot_function.__name__}.csv'
				df = pd.read_csv(name, sep=';')
				results = pd.concat([results, df], ignore_index=True)
	results.to_csv('results.csv', index=False, sep=';')


	# prepare results for plotting
	df = pd.DataFrame(results)
	grouped_df = df.groupby(['shuffle_rate', 'pivot_function', 'size'])['time'].mean().reset_index()

	unique_shuffle_rates = grouped_df['shuffle_rate'].unique()
	unique_pivot_functions = grouped_df['pivot_function'].unique()

	# plot results
	print('Number of plots: ', len(unique_shuffle_rates) * len(unique_pivot_functions))
	for pivot_function in unique_pivot_functions:
		for shuffle_rate in unique_shuffle_rates:
			subset_df = grouped_df[(grouped_df['pivot_function'] == pivot_function) & (grouped_df['shuffle_rate'] == shuffle_rate)]

			plt.plot(subset_df['size'], subset_df['time'], label=f'Shuffle Rate: {shuffle_rate}, Pivot Function: {pivot_function}', marker='o')

			plt.xlabel('Size')
			plt.ylabel('Time')
			plt.title(f'Mean Time for Each Size - Pivot Function: {pivot_function}')
			plt.legend()
			
			filename = f'plots/normal/{shuffle_rate}_{pivot_function}.png'
			plt.savefig(filename)
			
			plt.close()

	# plot results log

	for pivot_function in unique_pivot_functions:
		for shuffle_rate in unique_shuffle_rates:
			subset_df = grouped_df[(grouped_df['pivot_function'] == pivot_function) & (grouped_df['shuffle_rate'] == shuffle_rate)]

			plt.plot(subset_df['size'], subset_df['time'], label=f'Shuffle Rate: {shuffle_rate}, Pivot Function: {pivot_function}', marker='o')

			plt.xlabel('Size')
			plt.ylabel('Time')
			plt.xscale('log')
			plt.yscale('log')
			plt.title(f'Mean Time for Each Size - Pivot Function: {pivot_function}')
			plt.legend()
			
			filename = f'plots/logscale/{shuffle_rate}_{pivot_function}_log.png'
			plt.savefig(filename)
			
			plt.close()

	# comparison between pivot functions

	for shuffle_rate in unique_shuffle_rates:
		for pivot_function in unique_pivot_functions:
			subset_df = grouped_df[(grouped_df['pivot_function'] == pivot_function) & (grouped_df['shuffle_rate'] == shuffle_rate)]

			plt.plot(subset_df['size'], subset_df['time'], label=pivot_function, marker='o')
			
			plt.xlabel('Size')
			plt.ylabel('Time')
			plt.title(f'Mean Time for Each Size - Size: {size}')
			plt.legend()			
			
		filename = f'plots/comparison/{shuffle_rate}_log.png'
		plt.savefig(filename)
		plt.close()
