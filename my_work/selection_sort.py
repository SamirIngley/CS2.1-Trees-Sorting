

def selection(a_list):
# https://stackabuse.com/selection-sort-in-python/
    for item in range(len(a_list)):
        num = 0
        num_index = None
        for item2 in range(len(a_list)):
            if item2 > num:
                num = item
                num_index = a_list[item2]

        a_list[item] = num 
        a_list[num_index] = item
    
    print(a_list)
    return a_list


if __name__ == "__main__":

    listy = [1,3,4,2,6,4]
    selection(listy)