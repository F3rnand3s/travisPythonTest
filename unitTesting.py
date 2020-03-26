import unitst

class unitTesting(unittest.TestCase): 
    def setUp(self): 
        print 'some test 1'

    def test_search_in_python_org(self):
        print 'some test 2'

    def tearDown(self):
        print 'some test 3'

if __name__ == "__main__":
    unittest.main()
