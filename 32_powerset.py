"""
Power set P(S) of a set S is the set of all subsets of S. For example S = {a, b, c} then
P(s) = {{}, {a}, {b}, {c}, {a,b}, {a, c}, {b, c}, {a, b, c}}.
If S has n elements in it then P(s) will have 2^n elements

## powerset3 : DP solution go through this : https://www.youtube.com/watch?v=8cGQ9ocLYCU&t=1s
"""

def powerset(ps_input):
    subs = []
    total_comb = 2**len(ps_input)
    for i in range(total_comb):
        sub = []
        for j in range(len(ps_input)):
            if i & 1 << j:
                sub.append(ps_input[j])
        subs.append(sub)
    return subs

def powerset2(ps_input):
    result = [[]]
    for i in ps_input:
        newsubs = [j + [i] for j in result]
        result.extend(newsubs)
    return result

string = "abc"
print(powerset(list(string)))
print(powerset2(list(string)))
