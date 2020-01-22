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
    
if __name__ == "__main__":
    str1 = "team"
    str2 = "test"
    print("Lavestein distance b/w {} and {} : {}".format(str1, str2, distance_bw_string(str1,str2)))
