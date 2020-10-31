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
        
    print(flag)
    if (not flag): 
        return True
    return False



def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Swap adjacent items that are out of order

    n = len(items)

    for i in range(n - 1) :
        flag = 0

        for j in range(n - 1) :
            
            if items[j] > items[j + 1] : 
                tmp = items[j]
                items[j] = items[j + 1]
                items[j + 1] = tmp
                flag = 1

        if flag == 0:
            break
    return 

def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item
    for item in range(len(items)):
        num = 0
        num_index = None
        for item2 in range(len(items)):
            if item2 > num:
                num = item
                num_index = items[item2]

        items[item] = num 
        items[num_index] = item
    
    print(items)
    return items


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items
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

    # bubble_sort(nums)


   