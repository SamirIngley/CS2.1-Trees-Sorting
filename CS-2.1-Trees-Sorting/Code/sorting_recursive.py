#!python


def merge(array, left_index, right_index, middle):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    Running time: ??? Why and under what conditions?
    Memory usage: ??? Why and under what conditions?"""
    # Make copies of both arrays we're trying to merge
    # The second parameter is non-inclusive, so we have to increase by 1
    left_copy = array[left_index:middle + 1]
    right_copy = array[middle+1:right_index+1]

    # Initial values for variables that we use to keep
    # track of where we are in each array
    left_copy_index = 0
    right_copy_index = 0
    sorted_index = left_index

    # Go through both copies until we run out of elements in one
    while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):

        # If our left_copy has the smaller element, put it in the sorted
        # part and then move forward in left_copy (by increasing the pointer)
        if left_copy[left_copy_index] <= right_copy[right_copy_index]:
            array[sorted_index] = left_copy[left_copy_index]
            left_copy_index = left_copy_index + 1
        # Opposite from above
        else:
            array[sorted_index] = right_copy[right_copy_index]
            right_copy_index = right_copy_index + 1

        # Regardless of where we got our element from
        # move forward in the sorted part
        sorted_index = sorted_index + 1

    # We ran out of elements either in left_copy or right_copy
    # so we will go through the remaining elements and add them
    while left_copy_index < len(left_copy):
        array[sorted_index] = left_copy[left_copy_index]
        left_copy_index = left_copy_index + 1
        sorted_index = sorted_index + 1

    while right_copy_index < len(right_copy):
        array[sorted_index] = right_copy[right_copy_index]
        right_copy_index = right_copy_index + 1
        sorted_index = sorted_index + 1

def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half using any other sorting algorithm
    # TODO: Merge sorted halves into one list in sorted order
    pass

def merge_sort(array, left_index, right_index):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    Running time:  O(n log n) - merge doubles list size, n work for each step
    Memory usage: n length of array"""
    if left_index >= right_index:
        return

    middle = (left_index + right_index)//2
    merge_sort(array, left_index, middle)
    merge_sort(array, middle + 1, right_index)
    merge(array, left_index, right_index, middle)

def partition(a, low, high):
    i = low -1
    pivot = a[high]
    for j in range(low, high):
        if a[j] <= pivot:
            # swap
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[high] = a[high], a[i+1] 
    return i+1 

def quick_sort(a, low=0, high=None):
    ''' 
    Time Complexity: O(n log n) or O(n*n) worst case
    Memory: none, this is inplace
    ''' 
    if high == None:
        high = len(a) -1 
    if low < high:
        p_index = partition(a, low, high) # partition around pivot
        quick_sort(a, low, p_index-1) # sort lower half
        quick_sort(a, p_index+1, high) # sort upper half



if __name__ == "__main__":
    
    print("merge: ")
    mouse = [3, 6, 7, 4, 5, 3, 2, 1]
    print(mouse)
    merge_sort(mouse, 0, len(mouse)-1)
    print(mouse)

    print("quick:")
    ray = [5, 9, 1, 2, 4, 8, 6, 3, 7]
    print(ray)
    quick_sort(ray)
    print(ray)