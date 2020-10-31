#!python


def is_sorted(test_list):
    """Return a boolean indicating whether given items are in sorted order.
    Running time: O(n) bc we do a comparison for n items in the list
    Memory usage: """
    # Check that all adjacent items are in order, return early if so

    flag = 0
    i = 1
    while i < len(test_list): 
        if(test_list[i] < test_list[i - 1]): 
            flag = 1
        i += 1
        
    # print(flag)
    if (not flag): 
        return True
    return False



def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    Running time: O(n^2) This alg can only bring one item from one end to the other at a time. We need to make this loop n times worst case for every item
    Memory usage: Almost none because we're not creating any new values just rearranging them"""

    while not is_sorted(items):
        for i in range(len(items)-1):
            if items[i] > items[i+1]:
                items[i], items[i+1] = items[i+1], items[i]

    # print(items)
    return 

def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    Running time: O(n) goes through the list, finds the smallest number and puts it in the beginning every time - that's very efficient. We only loop through the array 1 time in theory. 
    Memory: None - we don't need any new memory, we simple rearrange/swap values. 
    """
    

    while not is_sorted(items):
        i = 1

        for ind, item in enumerate(items):
            # print(items)
            new_min = ind
            for j, item2 in enumerate(items[i:]):
                # print(items[i:])
                if item2 < item:
                    new_min = j+i
                    # print("item:", item, " min val:", item2)
            i += 1
            # print(i)

            # print("new_min at index: ", new_min)
            # print(items[ind], items[new_min])
            items[ind], items[new_min] = items[new_min], items[ind]

    # print(items)
    return items

    

def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: O(n^2) For each n we search through another set of n values. Worst case because we decrease the amount of unsorted values each time we progress thus getting faster. We have to loop through each number, then loop through the sorted list. 
    TODO: Memory usage: Why and under what conditions?"""
    
    for i in range(len(items)-1):
        j = i
        while j > 0 and items[j-1] > items[j]:
            items[j], items[j-1] = items[j-1], items[j]
            j = j-1

    print(items)
    return items


if __name__ == "__main__":
    
    nums = ([3, 2, 8, 5, 4, 3, 1])
    ascend = ([0, 2, 4, 5])
    descend = ([9, 3, 2, 1, 1])

    insertion_sort(nums)
    insertion_sort(ascend)
    insertion_sort(descend)



   