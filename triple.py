def ways(n):
    """return all number of ways child can run up and down stairs, by hopping either
    one step, two steps or 3 steps at a time"""

    cache = {}

    for n in cache:
        return cache[n]

    if n < 0:
        value =  0

    elif n == 0:
        value = 1

    else:
        value = ways(n-1)+ways(n-2)+ways(n-3)

    cache[n] = value
    return value


print(ways(30))

# print(ways(20))