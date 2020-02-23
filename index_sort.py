import random

def index_sort(array):

    positive_list = [x for x in array if x >= 0]
    negative_list = [x for x in array if x < 0]

    empty_positive_list = [None for x in range(max(positive_list)+1)]
    empty_negative_list = [None for x in range(abs(min(negative_list)-1))]

    for value in positive_list:
        if empty_positive_list[value] == None:
            empty_positive_list[value] = [value]
        else:
            empty_positive_list[value].append(value)

    for value in negative_list:
        if empty_negative_list[abs(value)] == None:
            empty_negative_list[abs(value)] = [value]
        else:
            empty_negative_list[abs(value)].append(value)

    sorted_positive_list = [x for x in empty_positive_list if x != None]
    sorted_negative_list = [x for x in empty_negative_list if x != None]
    sorted_negative_list.reverse()

    sorted_list_of_lists = sorted_negative_list + sorted_positive_list

    sorted_list = []

    for number_list in sorted_list_of_lists:
        for number in number_list:
            sorted_list.append(number)

    return sorted_list

unsorted_list = [random.randint(-10000,10000) for x in range(1000000)]
sorted_list = index_sort(unsorted_list)
