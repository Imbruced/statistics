def calculate_average(*values) -> float:
    return sum(values)/len(values)


def variance(*values) -> float:
    avg = calculate_average(*values)
    return sum([(el - avg)**2 for el in values])/len(values)


def median(*values) -> float:
    number_of_elements = len(values)
    sorted_elements = sorted(values)
    pivot = int(number_of_elements / 2)
    if number_of_elements % 2:
        median_value = sorted_elements[pivot]
    else:
        median_value = (sorted_elements[pivot] + sorted_elements[pivot-1])/2

    return median_value
