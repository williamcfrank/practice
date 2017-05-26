import unittest

"""
Implement an algorithm to determine if a string has all unique characters. What
if you cannot use additional data structures?

Notes:  Just keep track of all characters you see in a DS, if you see a repeat /
collision, return false.  Else return True.

"""

def is_unique(s):
    # Number of ascii characters is 128
    if len(s) > 128:
        return False
    char_set = [False for _ in range(0,127)]
    for char in s:
        val = ord(char)
        if char_set[val]:
            # Letter already found in string.
            return False
        char_set[val] = True
    return True

class Test(unittest.TestCase):
    dataT = [('abcd'), ('s4fad'), ('')]
    dataF = [('23ds2'), ('hb 627jh=j ()')]

    def test_is_unique(self):
        # true check
        for test_string in self.dataT:
            actual = is_unique(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = is_unique(test_string)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()
