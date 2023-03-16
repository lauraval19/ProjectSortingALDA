import time
from sortalgorithms import constants
from sortalgorithms import data_generator
from sortalgorithms.algorithms import selection_sort, insertion_sort, merge_sort


def take_execution_time(minimum_size, maximum_size, step, samples_by_size):
    """
    returns the table with median times
    """
    return_table = []

    for size in range(minimum_size, maximum_size + 1, step):
        table_row = [size]
        times = take_times(size, samples_by_size)
        return_table.append(table_row + times)

    return return_table


def take_times(size, samples_by_size):
    """
    It will return three values, one for each algorithm: The execution time for that size on each algorithm
    """
    samples = []
    for _ in range(samples_by_size):
        samples.append(data_generator.get_random_list(size))

    return [
        take_time_for_algorithm(samples, merge_sort),
        take_time_for_algorithm(samples, selection_sort),
        take_time_for_algorithm(samples, insertion_sort),
    ]


def take_time_for_algorithm(samples_array, sorting_approach):
    """
    Returns the median of the execution time measures for a sorting approach given in
    """
    times = []

    for sample in samples_array:
        start_time = time.time()
        sorting_approach(sample.copy())
        times.append(int(constants.TIME_MULTIPLIER * (time.time() - start_time)))

    times.sort()
    return times[len(times) // 2]
