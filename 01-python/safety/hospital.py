def draw_hospital(size=20):
    """
    Prints a hospital.
    :param size: number of size across.
    """
    print("-"*size*2)
    midpoint = round(size/2)
    for i in range(size-2):
        for j in range(size*2):
            if j == 0 or j == (size*2-1) or (j == size and i < (midpoint+2) and i > (midpoint -2) and i != midpoint):
                print("|", end="")
            elif i == midpoint and j > (midpoint*2-4) and j < (midpoint*2+4):
                print("-", end="")
            else:
                print(" ", end="")
        print("")
    print("-"*size*2)

if __name__ == '__main__':
    draw_hospital()
