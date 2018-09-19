import splitter
# import doctest

# nfail, ntests = doctest.testmod(splitter)

# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()
import unittest

class TestSplitFunction(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def testsimplestring(self):
        r = splitter.split()