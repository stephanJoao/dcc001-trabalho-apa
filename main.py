import numpy as np
import matplotlib.pyplot as plt

def shuffle_list():
	pass

def first_pos(arr, lo, hi):
	return lo

def middle_pos(arr, lo, hi):
	return (hi - lo) // 2 + lo

def random_pos(arr, lo, hi):
	return np.random.randint(lo, hi + 1)

def partition(arr, lo, hi, find_pivot):
	# choose pivot
	pivot_value = arr[find_pivot(arr, lo, hi)]

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

def quick_sort(arr, lo, hi, find_pivot):
	if lo >= 0 and hi >= 0 and lo < hi:	
		p = partition(arr, lo, hi, find_pivot)	
		quick_sort(arr, lo, p, find_pivot)
		quick_sort(arr, p + 1, hi, find_pivot)

def altera(arr):
	arr[0] = 10

if __name__ == "__main__":
	arr = list(np.random.randint(0, 100, 10))
	# arr = [5, 4, 3, 2, 1]
	print(arr)
	quick_sort(arr, 0, len(arr) - 1, random_pos)
	print(arr)
	
	

