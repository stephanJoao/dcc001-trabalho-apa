import numpy as np
import matplotlib.pyplot as plt
import time

# criação da lista embaralhada
def create_shuffled_list(size=10, shuffle_rate=0):
	arr = list(range(size))
	n_swaps = int(size * shuffle_rate)
	print(n_swaps)
	for i in range(n_swaps):
		a = np.random.randint(0, size)
		b = np.random.randint(0, size)
		arr[a], arr[b] = arr[b], arr[a]
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
		p = partition(arr, lo, hi, find_pivot)	
		quicksort(arr, lo, p, find_pivot)
		quicksort(arr, p + 1, hi, find_pivot)

# main
if __name__ == "__main__":
	shuffle_rates = [0.05, 0.25, 0.45]
	pivot_functions = [first_pos, middle_pos, median, random_pos, mean]
	n_experiments = 10
	
	l = create_shuffled_list(size=10000000, shuffle_rate=0.5)
	# print(l)
	# get processor time

	start = time.process_time()
	print('start: ', start)
	quicksort(l, 0, len(l) - 1, mean)
	end = time.process_time()
	print('end: ', end)
	
	# print(l)
	print('time: ', end - start)
	
	# sizes = [10**i for i in range(1, 6)]
	# print(sizes)
	# arr = list(np.random.randint(0, 100000, 100000))
	# arr = [5, 4, 3, 2, 1]
	# print(arr)
	# quicksort(arr, 0, len(arr) - 1, random_pos)
	# print(arr)