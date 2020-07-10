def make_division_by(n):
    """This closure returns a function that returns the division
       of an x number by n 
    """
    def division_by(x):
        return x/n

    return division_by

def run():
    division_by_3 = make_division_by(3)
    print(division_by_3(18))  # The expected output is 6

    division_by_5 = make_division_by(5)
    print(division_by_5(100))  # The expected output is 20

    division_by_18 = make_division_by(18)
    print(division_by_18(54))  # The expected output is 3


if __name__ == '__main__':
    import unittest

    class ClosureSuite(unittest.TestCase):
        def setUp(self):
            self.test_of_division_by_3 = {
                18: 6,
                33: 11,
                57: 19
            }

            self.test_of_division_by_5 = {
                30: 6,
                55: 11,
                95: 19
            }

            self.test_of_division_by_18 = {
                108: 6,
                198: 11,
                342: 19
            }

        def test_closure_make_division_by(self):
            for key, value in self.test_of_division_by_3.items():
                division_by_3 = make_division_by(3)
                result = division_by_3(key)
                self.assertEqual(value, result)

            for key, value in self.test_of_division_by_5.items():
                division_by_5 = make_division_by(5)
                result = division_by_5(key)
                self.assertEqual(value, result)
            
            for key, value in self.test_of_division_by_18.items():
                division_by_18 = make_division_by(18)
                result = division_by_18(key)
                self.assertEqual(value, result)
        
        def tearDown(self):
            del(self.test_of_division_by_3)
            del(self.test_of_division_by_5)
            del(self.test_of_division_by_18)

    run()
    unittest.main()
