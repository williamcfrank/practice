import unittest

"""
Return true if one string is a permutation of the other.

Notes: sort? if a string is a permutation of another string, then when I sort
them, the smaller string should be either fully contained in the larger one or
if they are the same size, then the sort should be the same.

Now this problem has become is it a subset of problem.  (order given) I think
there is a built in method for this.  O(nlogn) because of sorting. You can
verify if a string is a subset of another string in linear time by just scanning
through it once.
"""

def check_permutation(s1, s2):
    s1 = sorted(s1)
    s2 = sorted(s2)
    if len(s1) == len(s2):
        if s1 == s2:
            return True
        return False
    if len(s1) > len(s2):
        bigger = s1
        smaller = s2
    else:
        bigger = s2
        smaller = s1
    print(bigger)
    print(smaller)

if __name__ ==  "__main__":
    test_s1 = "helllllo"
    test_s2 = "lohe"
    check_permutation(test_s1, test_s2)
