import unittest

class unitesting(unittest.TestCase): 
    def setUp(self): 
        print 'some text 1'

    def test_search_in_python_org(self):
        print 'some text 2'

    def tearDown(self):
        print 'some text 3'

if __name__ == "__main__":
    unittest.main()