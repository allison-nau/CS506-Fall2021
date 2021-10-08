import pytest
from cs506 import matrix
import numpy as np

def test_matrix():
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
        my_det = round(matrix.get_determinant(your_array=the_array), 4)
        print(f"My answer: {my_det}")
        # Do the two numbers match:
        print(f"Is it a match? {test_answer == my_det}")