# index_sort
Sorting Algorithm that places a value of one list into the index of another list.

Eg.

unsorted_list = [4,6,1,3,1,6,13,535,23,6,0,-2,4,-5,-43,0,4,2]

Steps:

1- Split out positive and negative values into two lists:

positive_list = [4,6,1,3,1,6,13,535,23,6,0,4,0,4,2]

negative_list = [-2,-5,-43]

2- For each list, create a list of length m, where m is the max value in the list (absolute min value for the negative list), and fill them both with None (null) values:

empty_positive_list = [None<sub>0</sub>, None<sub>1</sub>, None<sub>2</sub> ... None<sub>534</sub>]

empty_negative_list = [None<sub>0</sub>, None<sub>1</sub>, None<sub>2</sub> ... None<sub>42</sub>]


3- Iterate through the positive and negative lists and input each value at the corresponding empty list index. The value should be inputted as a list to avoid removing duplicates:

positive_list = [4,6,1,3,1,6,13,535,23,6,0,4,0,4,2]
value = 4 --> empty_list[4]
value = 6 --> empty_list[6]
...
value = 2 --> empty_list[2]

empty_list = [[0, 0], [1, 1], [2], [3], [4, 4, 4], [6, 6, 6], [13], [23], [535]]

4- Flatten out the list of lists:

empty_list = [0, 0, 1, 1, 2, 3, 4, 4, 4, 6, 6, 6, 13, 23, 535]

5- Join the negative  and positive lists together (the negative list must be reversed in this step):

sorted_list = [-43, -5, -2, 0, 0, 1, 1, 2, 3, 4, 4, 4, 6, 6, 6, 13, 23, 535]


