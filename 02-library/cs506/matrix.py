# Import packages
import numpy as np


def get_determinant(your_array):
    # TODO
    # Initialize the determinant:
    the_det = None
    # Get dimensions of array:
    the_dim = your_array.shape
    if the_dim == (2, 2):
        # Calculate determinant:
        the_det = (your_array[0, 0] * your_array[1, 1]) - (your_array[1, 0] * your_array[0, 1])
    elif the_dim == (3, 3):
        the_det = (your_array[0, 0] * get_determinant(your_array[1:3, 1:3])) - \
                  (your_array[0, 1] * get_determinant(np.delete(your_array[1:3, :], axis=1, obj=1))) + \
                  (your_array[0, 2] * get_determinant(your_array[1:3, 0:2]))

        # TODO remove  print(your_array[:, [[0], [2]]])
    return the_det


def main_test():
    # TODO
    # Initialize numpy array:
    array_sizes_to_make = [[2, 2], [3, 3]]
    # loop over array sizes to try:
    for size in array_sizes_to_make:
        # Create array:
        print(f"Dimension of array: {size}")
        the_array = np.random.randint(-10, 10, size=(size[0], size[1]))
        the_array = the_array.astype(float)
        print("The array:")
        print(the_array)
        # Actual determinant using numpy:
        test_answer = round(np.linalg.det(the_array), 4)
        print(f"Answer using numpy to compare: {test_answer}")
        # Try my code:
        my_det = round(get_determinant(your_array=the_array), 4)
        print(f"My answer: {my_det}")
        # Do the two numbers match:
        print(f"Is it a match? {test_answer == my_det}")



if __name__ == '__main__':
    main_test()