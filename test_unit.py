import unittest

from main import convert_date

class TestDateConversion(unittest.TestCase):
    def test_convert_date(self):
        date_str = '2025-12-31'
        expected_result = ('31', '12', '2025')
        actual_result = convert_date(date_str)
        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()



from main import sum_list

class TestSumStringList(unittest.TestCase):

    def test_sum_string_list(self):
        string_list = ['1', '2', '3', '4', '5']
        result = sum_list(string_list)
        self.assertEqual(result, 15)


if __name__ == '__main__':
    unittest.main()




from main import sum_of_elements

class TestDivideSum(unittest.TestCase):
    def test_sum_of_elements(self):
        arr = [1, 2, 3, 4, 5, 6]
        result = sum_of_elements(arr)
        self.assertEqual(result, 0.4)

if __name__ == '__main__':
    unittest.main()

from main import combining_dictionaries

class TestMergeDicts(unittest.TestCase):
    def test_combining_dictionaries(self):
        dct1 = {
            'a': 1,
            'b': 2,
        }
        dct2 = {
            'c': 3,
            'd': 4,
        }
        expected_result = {
            'a': 1,
            'b': 2,
            'c': 3,
            'd': 4,
        }
        self.assertEqual(combining_dictionaries(dct1, dct2), expected_result)

if __name__ == '__main__':
    unittest.main()



from main import dictionary_sum

class TestDictionarySum(unittest.TestCase):

    def test_dictionary_sum(self):
        dct = {
            1: {
                1: 11,
                2: 12,
                3: 13,
            },
            2: {
                1: 21,
                2: 22,
                3: 23,
            },
            3: {
                1: 24,
                2: 25,
                3: 26,
            },
        }
        self.assertEqual(dictionary_sum(dct), 177)


if __name__ == '__main__':
    unittest.main()

from main import find_max_min

class TestFindMaxMin(unittest.TestCase):
    def test_find_max_min(self):
        numbers = [1, 4, 5, 9, 2, 8, 10]
        result = find_max_min(numbers)
        self.assertEqual(result, {'max': 10, 'min': 1})

    def test_empty_list(self):
        numbers = []
        result = find_max_min(numbers)
        self.assertIsNone(result)

    def test_one_item_list(self):
        numbers = [5]
        result = find_max_min(numbers)
        self.assertEqual(result, {'max': 5, 'min': 5})

if __name__ == '__main__':
    unittest.main()



from main import found_divisors
class TestFoundDivisors(unittest.TestCase):
    def test_found_divisors(self):
        self.assertEqual(found_divisors([1, 2, 3, 4, 5, 6]), [[1], [1, 2], [1, 3], [1, 2, 4], [1, 5], [1, 2, 3, 6]])

if __name__ == '__main__':
    unittest.main()





from main import generate_without_repetition

class TestGenerateNonRepeatingRandomNumbers(unittest.TestCase):
    def test_generate_without_repetition(self):
        N = 10
        start = 1
        end = 100
        result = generate_without_repetition(N, start, end)
        self.assertIsNotNone(result)
        self.assertEqual(len(result), N)
        for i in range(1, N):
            self.assertNotEqual(result[i], result[i - 1])

if __name__ == '__main__':
    unittest.main()


from main import get_random_color
class TestRandomColor(unittest.TestCase):
    def test_get_random_color(self):
        colors = ['red', 'green', 'blue', 'yellow', 'purple', 'orange', 'pink']
        color = get_random_color()
        self.assertIn(color, colors)

if __name__ == '__main__':
    unittest.main()




from main import shuffle_list

class TestShuffleList(unittest.TestCase):

    def test_shuffle_list(self):
        adding_values = [1, 2, 3, 4, 5, 6, 7, 8]
        shuf_list = shuffle_list(adding_values)
        self.assertNotEqual(adding_values, shuf_list)
        self.assertCountEqual(adding_values, shuf_list)

if __name__ == '__main__':
    unittest.main()