def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
        Modified from HW0
    """
        # Initialize array (list of lists) to store information:
    X = []
    # Open file using with so do not need to close later:
    with open(csv_file_path, "r") as my_file:
        lines = my_file.readlines()
        # For each lin in lines:
        for line in lines:
            # Check if line contains information:
            if len(line) > 0:
                # # Replace commas between double quotes with -------------------------------------------------------
                # # (This is done for exercise 4)
                # # Split by double quotes:
                # temp_split = line.split(sep='"')
                # t_len = len(temp_split)
                # if t_len > 1:
                #    for i in range(t_len):
                #        # Only replace ones in odd number indices:
                #        if i % 2 == 1:
                #            temp_split[i] = temp_split[i].replace(",", ";")
                ## Rejoin together:
                # line = "".join(temp_split)
                # End replacing commas between double quotes ------------------------------------------------------
                # Convert line into list, splitting by commas and stripping undesired characters:
                line = line.strip("\n").split(sep=",")
                # Append to appropriate lists:
                X.append(line)
    X = convert_to_numeric(X)
    return X

def convert_to_numeric(a):
    """
    Converts string values to numeric values in array "a". Strips "" from strings
    :param a: 2D array (list of lists).
    :return: cleaned array.
    Modified from HW0
    """
    # For each line in array, convert to numeric
    for i in range(len(a)):
        for j in range(len(a[0])):
            try:
                # TODO: should this be int or float?
                a[i][j] = int(a[i][j])
            except ValueError:
                a[i][j] = a[i][j].strip('"')
    return a