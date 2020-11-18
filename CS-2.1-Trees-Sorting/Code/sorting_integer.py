#!python

def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum integer values)
    upper = max(numbers)
    lower = min(numbers)
      
    # TODO: Create list of counts with a slot for each number in input range
    counts = {}
    for count in range(lower, upper+1):
      counts[count] = 0 

    # TODO: Loop over given numbers and increment each number's count
    for item in numbers:
      counts[item] += 1

    # TODO: Loop over counts and append that many numbers into output list
    output_list = []
    for key, value in counts.items():
      for item in range(value):
        output_list.append(key)

    print('Output List: ', output_list)
    # Stretch: Improve this to mutate input instead of creating new output list
    # for index in range(len(numbers)-1):

    #   for key, value in counts.items():
    #   numbers[index] = 

    #TODO: Write some test cases
    return numbers


def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

    # TODO: Find range of given numbers (minimum and maximum values)
    min_val = None
    max_val = None 
    for i, item in enumerate(numbers):
        if i == 0:
            min_val = item
            max_val = item 
        else:
            if item > max_val:
                max_val = item
            if item < min_val:
                min_val = item 

            
    # TODO: Create list of buckets to store numbers in subranges of input range
    # TODO: Loop over given numbers and place each item in appropriate bucket
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    # TODO: Loop over buckets and append each bucket's numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list

    # Value * Number_of_Elements / (Maximum_Array_Value + 1) = bucket

if __name__ == "__main__":
  numbs = [0, 5, 2, 9, 3, 1, 5, 6, 3]
  counting_sort(numbs)
