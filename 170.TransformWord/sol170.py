import os

def word_distance(first, second):
    """compute number of differing characters in two words of the same length"""
    zipped = zip(list(first), list(second))
    diff = filter(lambda x: x[0] != x[1], zipped)
    return len(list(diff))


def construct_adjacency_list(dic):
    """for each word in dic, add the word and the list of words that are one character away to a hash"""
    res = {}
    for word in dic:
        res[word] = [x for x in dic if word_distance(x, word) == 1]
    return res

def solve(start, end, dic):
    # in the example the dictionary does not contain the start word, add it
    dic_with_start = dic.copy()
    dic_with_start.add(start)
    adjacency_list = construct_adjacency_list(dic_with_start)
    print("adj list: %s" % adjacency_list)
    work_list = []
    work_list.append([start])
    while work_list:
        new_list = []
        print("work list: %s" % work_list)
        for temp_list in work_list:
            last_word = temp_list[-1]
            for word in adjacency_list[last_word]:
                if word == end:
                    # solution found
                    temp_list.append(end)
                    return temp_list
                if word not in temp_list:
                    # reachable word not used yet, append
                    longer_list = temp_list.copy()
                    longer_list.append(word)
                    new_list.append(longer_list)
                # word already used, dead end, drop
        work_list = new_list
    # if we are here, no solution
    return None

# main
print("i am main")
start_word = "dog"
end_word = "cat"
dic = {"dot", "dop", "dat", "cat"}
res = solve(start_word, end_word, dic)
print("res: %s" % res)
