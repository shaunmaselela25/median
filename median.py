#  code for finding the median of a list of floats

def findMedian(L):
    """Finds median of L.
    L: a non-empty list of floats
    Returns:
    If L has an odd number of elements, returns the median
    element of L. For example, if L is the list
    [15.0, 5.3, 18.2], returns 15.0.
    If L has an even number of elements, returns the average
    of the two median elements. For example, if L is the
    list [1.0, 2.0, 3.0, 4.0], returns 2.5.
    If the list is empty, raises a ValueError exception.
    Side effects: none.
    """
    if len(L) == 0:
        raise ValueError("List is empty")
    sorted_L = sorted(L)
    n = len(sorted_L)
    mid = n // 2
    if n % 2 == 1:
        return sorted_L[mid]
    else:
        return (sorted_L[mid - 1] + sorted_L[mid]) / 2  
    
# Example usage:
if __name__ == "__main__":
    data = [3.5, 2.1, 5.6, 4.3]
    print("Median:", findMedian(data))  # Output: Median: 3.9   

    
