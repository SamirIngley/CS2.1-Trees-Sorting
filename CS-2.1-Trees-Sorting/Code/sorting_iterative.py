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
    TODO: Running time: O(n^2) Worst case because the loop will run for n items, and this will occur as many times as the n items. 
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Swap adjacent items that are out of order

    while not is_sorted(items):
        for i in range(len(items)-1):
            if items[i] > items[i+1]:
                items[i], items[i+1] = items[i+1], items[i]

    # print("Bubble:")
    # print(items)
    return 

def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item

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

    selection_sort(nums)
    # selection_sort(ascend)
    # selection_sort(descend)



   