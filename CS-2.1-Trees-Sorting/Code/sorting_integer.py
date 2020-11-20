#!python

from sorting_iterative import insertion_sort

def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    Running time: Linear Time
    Memory usage: ??? Why and under what conditions?"""
    # Find range of given numbers (minimum and maximum integer values)
    upper = max(numbers)
    lower = min(numbers)
      
    # Create list of counts with a slot for each number in input range
    counts = {}
    for count in range(lower, upper+1):
      counts[count] = 0 

    # Loop over given numbers and increment each number's count
    for item in numbers:
      counts[item] += 1

    # Loop over counts and append that many numbers into output list
    output_list = []
    for key, value in counts.items():
      for item in range(value):
        output_list.append(key)

    print('Counting Input: ', numbers)
    print('Counting Sorted List: ', output_list)

    # Stretch: Improve this to mutate input instead of creating new output list
    # for index in range(len(numbers)-1):

    #   for key, value in counts.items():
    #   numbers[index] = 

    #TODO: Write some test cases
    return numbers


def bucket_sort(numbers, num_buckets=10):
  """Sort given numbers by distributing into buckets representing subranges,
  then sorting each bucket and concatenating all buckets in sorted order.
  Running time: Linear Time, insertion sort is really fast for small sets
  Memory usage: """

  # Find range of given numbers (minimum and maximum values)
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
  
  # Create list of buckets to store numbers in subranges of input range
  buckets = {}
  for item in range(num_buckets):
    buckets[item] = []

  # Loop over given numbers and place each item in appropriate bucket
  for item in numbers:
    if abs(item) > 9:
      first = item[0]
      buckets[first].append(item)
    else:
      buckets[item].append(item)

  # Sort each bucket using any sorting algorithm (recursive or another)
  for key, value in buckets.items():
    if len(value) > 0:
      buckets[key] = insertion_sort(value)

  sorted_list = []
  # Loop over buckets and append each bucket's numbers into output list
  for key, value in buckets.items():
    for item in value:
      sorted_list.append(item)

  # Improve this to mutate input instead of creating new output list

  # Value * Number_of_Elements / (Maximum_Array_Value + 1) = bucket
  print('Buckets: ', buckets)
  print('Bucket Sorted List: ', sorted_list)

  return sorted_list

if __name__ == "__main__":
  numbs = [0, 5, 2, 9, 3, 1, 5, 6, 3]
  counting_sort(numbs)
  bucket_sort(numbs)
