import unittest
import random

def insertion_sort(arr):
    # iterate though len
    for i in range(1, len(arr)):
        key = arr[i]

        # move elements that are greater than the key
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            arr[j + 1] = key


class TestInsertionSort(unittest.TestCase):

    def test_small_array(self):
        arr = [5, 2, 8, 3, 1]
        insertion_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 5, 8])

    def test_large_array(self):
        arr = [random.randint(1, 1000) for _ in range (1000)]
        sorted_arr = sorted(arr)
        insertion_sort(arr)
        self.assertEqual(arr, sorted_arr)

    def test_nearly_sorted(self):
        arr = [i for i in range(100)]
        random.shuffle(arr)
        insertion_sort(arr)
        self.assertEqual(arr, [i for i in range(100)])

    def test_reversed_array(self):
        arr = [i for i in range(100, 0, -1)]
        insertion_sort(arr)
        self.assertEqual(arr, [i for i in range(1, 101)])

if __name__ == '__main__':
    unittest.main()