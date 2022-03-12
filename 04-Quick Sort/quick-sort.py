
def quick_sort (arr):
    """
    perform quick sort algorithm on a given array
   
    Args:
        (arr) arr - array to perform selection sort on
    
    Returns:
        (arr) arr - the sorted array
    """
	# test for the base case, if array length is 0 or 1
    if (len(arr) < 2):
        return arr
	
	# do recursive partitioning and quick sort 
    else:
        pivot = arr[0]
		
		# partition elements less or greater than pivot to sub-arrays
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot] 
		
		# repeat patitioning on the less and greater elements 
        return (quick_sort(less) + [pivot] + quick_sort(greater))
		

# algorithm test
quick_sort([1, 5, 2, 4])

