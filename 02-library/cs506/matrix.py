# Import packages
import numpy as np


def get_determinant(your_array):
    # TODO
    # Get dimensions of array:
    the_dim = your_array.shape
    if the_dim == (2, 2):
        # Calculate determinant:
        the_det = (your_array[0, 0] * your_array[1, 1]) - (your_array[1, 0] * your_array[0, 1])
    return the_det


def main_test():
    # TODO
    # Initialize numpy array:
    array_sizes_to_make = [[2, 2]]
    # loop over array sizes to try:
    for size in array_sizes_to_make:
        # Create array:
        print(f"Dimension of array: {size}")
        the_array = np.random.randint(-10, 10, size=(size[0], size[1]))
        the_array = the_array.astype(float)
        print("The array:")
        print(the_array)
        # Actual determinant using numpy:
        test_answer = np.linalg.det(the_array)
        print(f"Answer using numpy to compare: {test_answer}")
        # Try my code:
        my_det = get_determinant(your_array=the_array)
        print(f"My answer: {my_det}")
        # Do the two numbers match:
        print(f"Is it a match? {test_answer == my_det}")



if __name__ == '__main__':
    main_test()