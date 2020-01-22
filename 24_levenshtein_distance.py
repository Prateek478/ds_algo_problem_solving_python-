'''
Find the Levenshtein Distance between two strings to transfer one string to another
For example, from "test" to "test" the Levenshtein distance is 0 because both the source and
target strings are identical. No transformations are needed. In contrast, from "test" to "team"
the Levenshtein distance is 2 - two substitutions have to be done to turn "test" in to "team".
'''

def distance_bw_string(str1, str2):
    total_diff = 0
    if len(str1) != len(str2):
        print("Error : strings as length are not equal.")
        return

    for i in range(len(str1)):
        if str1[i] != str2[i]:
            total_diff += 1
    return total_diff


def levenshtein_numpy(seq1, seq2):
    size_x = len(seq1) + 1
    size_y = len(seq2) + 1
    matrix = np.zeros((size_x, size_y))
    for x in range(size_x):
        matrix[x, 0] = x
    for y in range(size_y):
        matrix[0, y] = y

    for x in range(1, size_x):
        for y in range(1, size_y):
            if seq1[x - 1] == seq2[y - 1]:
                matrix[x, y] = min(
                    matrix[x - 1, y] + 1,
                    matrix[x - 1, y - 1],
                    matrix[x, y - 1] + 1
                )
            else:
                matrix[x, y] = min(
                    matrix[x - 1, y] + 1,
                    matrix[x - 1, y - 1] + 1,
                    matrix[x, y - 1] + 1
                )
    print (matrix)
    return (matrix[size_x - 1, size_y - 1])
    
if __name__ == "__main__":
    str1 = "team"
    str2 = "test"
    print("Lavestein distance b/w {} and {} : {}".format(str1, str2, distance_bw_string(str1,str2)))
    print("Lavestein distance b/w {} and {} : {}".format(str1, str2, levenshtein_numpy(str1,str2)))
    
