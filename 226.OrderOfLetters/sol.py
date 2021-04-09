"""
This problem was asked by Airbnb.

You come across a dictionary of sorted words in a language 
you've never seen before. Write a program that returns the 
correct order of letters in this language.

For example, given ['xww', 'wxyz', 'wxyw', 'ywx', 'ywz'], 
you should return ['x', 'z', 'w', 'y'].
"""

def split_by_first_letter(words):
    result = list()
    h = {}
    for word in words:
        first_letter = word[0]
        if first_letter not in h:
            h[first_letter] = list()
        h[first_letter].append(word[1:])
    for letter in h:
        result.append(h[letter])
    return result

# collect ordered pairs into "pairs"
def collect_pairs(words, pairs):
    if len(words) < 2:
        return
    seen_letters = set()
    for word in words:
        seen_letters.add(word[0])
        for seen_letter in seen_letters:
            if seen_letter != word[0]:
                pairs.append([seen_letter, word[0]])
    sub_words = split_by_first_letter(words)
    for sub_word in sub_words:
        collect_pairs(sub_word, pairs)

# collect sets of letters that are smaller than other letters
# ([x,y], [x,w]) -> { x -> [y,w] }
def process_pairs(pairs):
    res = {}
    for pair in pairs:
        larger, smaller = pair
        if larger not in res:
            res[larger] = set()
        res[larger].add(smaller)
    return res

def collect_smaller(hh, letter):
    res = set()
    # smallest letter will not be in hh
    if letter in hh:
        for sm in hh[letter]:
            res.add(sm)
            res.update(collect_smaller(hh, sm))
    return res

def transitive_close(hh):
    changes = True
    while changes:
        changes = False
        for letter in hh:
            new_set = collect_smaller(hh, letter)
            if len(new_set.difference(hh[letter])) > 0:
                hh[letter] = new_set
                changes = True
    pass

def set_of_all_characters(words):
    result = set()
    for word in words:
        for letter in word:
            result.add(letter)
    return result

input_words = ['xww', 'wxyz', 'wxyw', 'ywx', 'ywz']

pairs = list()

collect_pairs(input_words, pairs)

#print("pairs: %s" % pairs)

hh = process_pairs(pairs)

#print("processed pairs: %s" % hh)

closure = transitive_close(hh)

#print("closure: %s" % hh)

# sort letters by number of letters following them
# gets [('x', {'w', 'y', 'z'}), ('z', {'w', 'y'}), ('w', {'y'})]
sorted_closure = sorted(hh.items(), key=lambda x: len(x[1]), reverse=True)

# extract order of letters that have at least one letter that is smaller
ordered_lets = list(map(lambda x: x[0], sorted_closure))

#print("ordered lets: %s" % ordered_lets)

# create a set of letters that are larger than at least one so we can find missing letter(s)
ordered_set = set()
ordered_set.update(ordered_lets)
missing_set = set_of_all_characters(input_words) - ordered_set

#print("missing set: %s" % missing_set)
# add letters that do not have letters smaller than them (we must have at least one)
ordered_lets.extend(missing_set)

print("res: %s" % ordered_lets)

exit(0)

