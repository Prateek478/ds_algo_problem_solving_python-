"""
Group Anagrams from given list
Anagrams are the words that are formed by similar elements but the orders in which these characters occur differ
Example:
The original list : ['lump', 'eat', 'me', 'tea', 'em', 'plum']
The grouped Anagrams : [['me', 'em'], ['lump', 'plum'], ['eat', 'tea']]
"""

def group_anagrams(lst):
    occurances = dict()
    for i in lst:
        sort_input = "".join(sorted(i))
        if sort_input in occurances.keys():
            occurances[sort_input].append(i)
        else:
            occurances[sort_input] = list()
            occurances[sort_input].append(i)
    return occurances.values()

def group_anagrams_2(lst):
    from itertools import groupby
    temp = lambda test_list : sorted(test_list)
    result = []
    for key, val in groupby(sorted(lst, key=temp), temp):
        result.append(list(val))
    return result

if __name__ == "__main__":
    print (group_anagrams(['lump', 'eat', 'me', 'tea', 'em', 'plum']))
    print (group_anagrams_2(['lump', 'eat', 'me', 'tea', 'em', 'plum']))
