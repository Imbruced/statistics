import logging

from functions import calculate_average, variance, median

if __name__ == "__main__":
    assert calculate_average(1.0, 2.0) == 1.5
    assert calculate_average(1.0, 3.0) == 2.0
    assert calculate_average(1.0, 1.0) == 1.0
    assert calculate_average(2.0, 4.0) == 3.0
    assert calculate_average(2.0, 6.0) == 4.0
    assert calculate_average(1.0, 2.0, 4.23, 2.34) == 2.3925
    assert variance(1.0, 2.0) == 0.25
    assert median(1.0, 4.0, 2.0) == 2.0
    assert median(8.0, 1.0, 4.0, 2.0) == 3.0
    logging.info("all tests passed")
