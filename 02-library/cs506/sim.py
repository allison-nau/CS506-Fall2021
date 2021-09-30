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
        distance = 1
    return distance

def cosine_sim(x, y):
    raise NotImplementedError()

# Feel free to add more
