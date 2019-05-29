def rsum(list):
    sum = 0
    if len(list) == 1:
        sum = list[0]
    else:
        sum = list[0] + rsum(list[1:])
    return sum


def rmax(list):
    if(len(list) == 1):
        max = list[0]
    else:
        max = rmax(list[1:])
        if(max < list[0]):
            max = list[0]
    return (max)


def two_smallest_tuple(list1):
    if(len(list1) == 2):
        if (list1[0] <= list1[1]):
            tup = (list1[0], list1[1])
        else:
            tup = (list1[1], list1[0])
    else:
        (first_smallest, second_smallest) = two_smallest_tuple(list1[1:])
        if (list1[0] < first_smallest):
            tup = (list1[0], first_smallest)
        elif (list1[0] < second_smallest):
            tup = (first_smallest, list1[0])
        else:
            tup = (first_smallest, second_smallest)
    return tup


def second_smallest(list1):
    second = two_smallest_tuple(list1)
    second = second[1]
    return second


def sum_max_min(list):
    smallest = two_smallest_tuple(list)
    smallest = smallest[0]
    return(rmax(list) + smallest)
