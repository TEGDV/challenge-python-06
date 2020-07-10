def make_division_by(n):
    def divider(x):
        assert type(x) == int
        return x / n

    return divider


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
            self.test = {
                8:(3,24),
                1:(100,100),
                2:(10,20),
                3:(3,9),
                4:(20,80)
            }

        def test_closure_make_division_by(self):
            # Make the closure test here
            for key, value in self.test.items():
                divisor_n = make_division_by(value[0])
                print(divisor_n(value[1]))
                self.assertEqual(key, divisor_n(value[1]), 'Check your functions')
        
        def tearDown(self):
            del(self.test)

    run()
    unittest.main()