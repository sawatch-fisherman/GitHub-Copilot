def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == target:
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1

    return None


arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 11

result = binary_search(arr, target)

if result is not None:
    print(f"Target {target} found at index: {result}")
else:
    print(f"Target {target} not found in the array.")


import unittest

class TestBinarySearch(unittest.TestCase):
    def test_binary_search_found(self):
        arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
        target = 11
        expected = 5
        result = binary_search(arr, target)
        self.assertEqual(result, expected)

    def test_binary_search_not_found(self):
        arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
        target = 3
        expected = None
        result = binary_search(arr, target)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()