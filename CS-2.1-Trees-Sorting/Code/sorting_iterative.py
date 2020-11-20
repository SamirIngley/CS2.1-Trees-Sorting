#!python


def is_sorted(a_list):
    """Return a boolean indicating whether given items are in sorted order.
    Running time: O(n) bc we do a comparison for n items in the list
    Memory usage: None, no memory created """
    # Check that all adjacent items are in order, return early if so

    if len(a_list) == 1 or len(a_list) == 0:
        return True 
    else:
        previous = a_list[0]

        for item in a_list:
            if item < previous:
                return False
            previous = item

    return True



def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    Running time: O(n^2) This alg can only bring one item from one end to the other at a time. We need to make this loop n times worst case for every item
    Memory usage: Almost none because we're not creating any new values just rearranging them"""

    # check if it items are sorted after each iteration 
    while not is_sorted(items):

        # I chose to iterate via index of each item
        for i in range(len(a_list)-1):
            if items[i+1] < items[i]:
                #swap
                items[i], items[i+1] = items[i+1], items[i]

    # print(items)
    return 

def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    Running time: O(n^2) We have to find the smallest item every time to compare. So that's n * n. 
    Memory: None - we don't need any new memory, we simple rearrange/swap values. 
    """
    
    while not is_sorted(items):
        i = 1

        # two loops: one to loop through each place in the items, the other to find the minimum element each time. 
        for ind, item in enumerate(items):
            new_min = ind
            # find the minimum value in the list of items
            for j, item2 in enumerate(items[i:]):

                # the index is from the beginning of the list of items, not from where the loop began
                if item2 < item:
                    new_min = j+i
            i += 1

            # swap the new min with the current index of the outer loop
            items[ind], items[new_min] = items[new_min], items[ind]

    # print(items)
    return items

    

def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: O(n^2) For each n we search through another set of n values. Worst case because we decrease the amount of unsorted values each time we progress thus getting faster. We have to loop through each number, then loop through the sorted list. 
    TODO: Memory usage: None """
    
    for index in range(1, len(items)):
        currVal = items[index]
        currPos = index 

        while currPos > 0 and items[currPos -1] > currVal:
            items[currPos] = items[currPos -1]
            currPos = currPos -1 
        
        items[currPos] = currVal

    # print(items)
    return items


if __name__ == "__main__":
    
    nums = ([3, 2, 8, 5, 4, 3, 1])
    ascend = ([0, 2, 4, 5])
    descend = ([9, 3, 2, 1, 1])

    insertion_sort(nums)
    insertion_sort(ascend)
    insertion_sort(descend)
