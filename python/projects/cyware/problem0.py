numalpha_map = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}


def int_to_str(value: int) -> str:
    nums = [int(i, 16) for i in value]
    out = []

    for n in nums:
        if n == '-':
            out.append(nums[0])
        else:
            out.append(numalpha_map[n])

    return ''.join(out)


# should print "5"
print(int_to_str(5))

# should print "50"
print(int_to_str(50))

# should print "500"
print(int_to_str(500))

# should print "-5"
print(int_to_str(-5))

# should print "-50"
print(int_to_str(-50))

# should print "-500"
print(int_to_str(-500))

# -- Test Case --
import unittest


class IntToStringTestCase(unittest.TestCase):

    def setUp(self) -> None:
        return super().setUp()

    def test_int_to_str(self):
        pass

    def tearDown(self) -> None:
        return super().tearDown()


unittest.main(argv=[''], verbosity=2, exit=False)
