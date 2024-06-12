# バブルソートのコード

# バブルソートの関数
def bubble_sort(numbers):
    """バブルソートの関数
    Args:
        numbers (list): 並び替える数値のリスト
    Returns:
        list: 並び替えた数値のリスト
    """ 
    for i in range(len(numbers) - 1): # 修正: 最後の要素は比較する必要がないため、範囲を1つ減らす
        for j in range(len(numbers) - i - 1): # 修正: 各イテレーションで最後の要素は既にソートされているため、範囲を狭める
            if numbers[j] > numbers[j + 1]:
                # swap
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j] # 修正: 正しい要素で交換する
    return numbers # 並び替えたリストを返す

import unittest
from sort_1 import bubble_sort

class TestBubbleSort(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(bubble_sort([]), [])

    def test_single_element_list(self):
        self.assertEqual(bubble_sort([1]), [1])

    def test_already_sorted_list(self):
        self.assertEqual(bubble_sort([1, 2, 3]), [1, 2, 3])

    def test_reverse_sorted_list(self):
        self.assertEqual(bubble_sort([3, 2, 1]), [1, 2, 3])

    def test_unsorted_list(self):
        self.assertEqual(bubble_sort([2, 3, 1]), [1, 2, 3])

    def test_duplicate_elements(self):
        self.assertEqual(bubble_sort([2, 3, 3, 1]), [1, 2, 3, 3])

    def test_negative_numbers(self):
        self.assertEqual(bubble_sort([-2, -3, -1]), [-3, -2, -1])

if __name__ == '__main__':
    unittest.main()

# バブルソートの関数を呼び出す
if __name__ == '__main__':
    import random
    numbers = [random.randint(0, 1000) for _ in range(10)]
    print(numbers)
    bubble_sort(numbers)
    print(numbers)
    test_bubble_sort()