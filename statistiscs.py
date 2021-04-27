from math import ceil


def mean(values):
    """
    return the mean of values
    :param values: list of numeric values
    :return: the mean of values
    """
    sum = 0
    for value in values:
        sum += value
    return sum/len(values)


def median(values):
    """
    return the median of values
    :param values: list of numeric values
    :return: median of values
    """
    values.sort()
    n = len(values)
    if n % 2 == 0:
        med = values[(n//2)-1] + values[n//2]
        med /= 2
    else:
        med = values[ceil(n/2)-1]
    return med
