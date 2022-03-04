
def selection_sort (arr, arr_len):
    """
    perform selection sort algorithm on a given array
   
    Args:
        (arr) arr     - array to perform selection sort on
        (int) arr_len - length of the array that is to be sorted
    
    Returns:
        (arr) arr - the sorted array
    """
    for i in range (arr_len):
        # assume the first element is the smallest
        min_i = i
        
        # compare each of the elements to find the smallest
        for j in range ((i + 1), arr_len):
            if arr[min_i] > arr[j]:
                min_i = j
                
        # swap the smallest element to a earlier index 
        temp = arr[i]
        arr[i] = arr[min_i]
        arr[min_i] = temp
    
    return arr
        

# algorithm test
selection_sort([1, 5, 2, 4], 4)

