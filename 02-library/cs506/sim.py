def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += abs(x[i] - y[i])
    return res

def jaccard_dist(x, y):
    total = 0
    similar = 0
    for i in range(len(x)):
        total += 1
        if x[i] == y[i]:
            similar += 1
    if total != 0:
        distance = 1 - (similar/total)
    else:
        distance = 1  # TODO: Does this make sense?
    return distance

def cosine_sim(x, y):
    # Based on:
    # https://stackoverflow.com/questions/18424228/cosine-similarity-between-2-number-lists
    sum_xx = 0
    sum_yy = 0
    sum_xy = 0
    for i in range(len(x)):
        sum_xx += x[i]*x[i]
        sum_yy += y[i]*y[i]
        sum_xy += x[i]*y[i]
    if sum_xx != 0 and sum_yy != 0:
        distance = sum_xy / ((sum_xx * sum_yy) ** (1/2))
    else:
        distance = 0  # TODO: Does this make sense?
    return distance


# Feel free to add more