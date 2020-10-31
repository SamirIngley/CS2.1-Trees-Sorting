
def insertion(a_list):
    
    for i in range(len(a_list)-1):
        j = i
        while j > 0 and a_list[j-1] > a_list[j]:
            a_list[j], a_list[j-1] = a_list[j-1], a_list[j]
            j = j-1

    print(a_list)

if __name__ == "__main__":
    
    listy = [0, 2, 4, 5, 3, 2]
    insertion(listy)