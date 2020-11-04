
# split array into smaller arrays by half until they are individual numbers

# base case: when list length is 1 (already sorted)

# https://stackabuse.com/merge-sort-in-python/

def merge_sort(array):

    if len(array) == 1: # a list of 1 is already sorted
        print('array' + array)
        return array 
    
    # recursive case
    middle = (len(array)) // 2
    print('middle ', middle)

    # give me left chunk and right chunk
    left = array[0:middle+1]
    right = array[middle+1:]
    print(left)
    print(right)
    input()

    result_left = merge_sort(left)
    result_right = merge_sort(right)

    return merge(result_left, result_right)

def merge(left, right):

    merged = []
    lindex = 0
    rindex = 0

    if len(left) >= len(right):
        longer = len(left)
    else:
        longer = len(right)

    # loop through the longer string
    for item in range(len(longer)-1):
        if left[lindex] == right[rindex]: 
            merged.append(left[lindex])
            merged.append(right[rindex])
        # if the left index is greater than right, append it
        elif left[lindex] > right[rindex]:
            merged.append(left[lindex])
        else:
            merged.append(right[rindex])

    print(merged)
    return merged 

if __name__ == "__main__":

    merge_sort([8, 1, 9, 14, 23])

