

import numpy as np

def calculate(list):

    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")

    my_array = np.array(list)####

    matrix = my_array.reshape((3,3))####

    mean_flattern = np.mean(my_array).tolist()

    mean_rows = np.mean(matrix , axis=1).tolist()

    mean_column = np.mean(matrix , axis=0).tolist()

    variance_flattern = np.var(my_array).tolist()

    variance_rows = np.var(matrix , axis=1).tolist()

    variance_column = np.var(matrix , axis=0).tolist()

    std_flattern = np.std(my_array).tolist()

    std_rows = np.std(matrix, axis=1).tolist()

    std_column = np.std(matrix , axis=0).tolist()

    max_flattern = np.max(my_array).tolist()

    max_row = np.max(matrix , axis=1).tolist()

    max_column = np.max(matrix , axis=0).tolist()

    min_flattern = np.min(my_array).tolist()

    min_row = np.min(matrix , axis=1).tolist()

    min_column = np.min(matrix , axis=0).tolist()

    sum_flattern = np.sum(my_array).tolist()

    sum_row = np.sum(matrix , axis=1).tolist()

    sum_column = np.sum(matrix , axis=0).tolist()

    result = {
        'mean': [mean_column, mean_rows, mean_flattern],
        'variance': [variance_column, variance_rows, variance_flattern],
        'standard deviation': [std_column, std_rows, std_flattern],
        'max': [max_column, max_row, max_flattern],
        'min': [min_column, min_row, min_flattern],
        'sum': [sum_column,sum_row , sum_flattern]
    }

    return result


    
