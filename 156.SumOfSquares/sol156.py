import os

def collect_candidates(n):
    """ create a list of numbers with squared less than n """
    res = [ x*x for x in range(1,n) if x*x <= n]
    return res

def find_sol(n, target, parts, length_so_far):
    # print("find_sol: %d, %s, %d" % (target, parts, length_so_far))
    if target == 0:
        # we are done
        return length_so_far
    min = n
    for part in parts:
        if target >= part:
            res = find_sol(n, target - part, parts, length_so_far + 1)
            if res < min:
                min = res
    return min


def solve(n):
    parts = collect_candidates(n)
    res = find_sol(n, n, parts, 0)
    return res

def test(n, expected):
    res = solve(n)
    print("res(%d) = %d (%s)" % (n, res, "correct" if res == expected else "incorrect")) 

test(13,2)
test(27, 3)
