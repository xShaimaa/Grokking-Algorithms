
def binary_search (arr, item, low, high):
    """
    find an item on a given list within specified range 
    using binary search algorithm in a recursive manner
   
    Args:
        (arr) arr  - array to search within
        (int) item - number we are searching for
        (int) low  - array start index
        (int) high - array end index
    
    Returns:
        (int) index - the desired item index
        (int)  -1   - if item not found
    """
    # validate base case
    while (low <= high):
        # check the middle element
        mid = (low + high) // 2
        guess = arr[mid]
      
        # if the guess is a match
        if guess == item:
            return mid
    
        # if the guess is too high.
        if guess > item:
            return binary_search(arr, item, mid - 1, high)
        
        # if the guess is too low.
        else:
            return binary_search(arr, item, mid + 1, high)

    # if item doesn't exist
    return -1

# algorithm test
binary_search([1, 3, 4, 7], 3, 0, 3)

