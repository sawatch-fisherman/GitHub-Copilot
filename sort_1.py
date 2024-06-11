# バブルソートのコード

# バブルソートの関数
def bubble_sort(numbers):
    """バブルソートの関数
    Args:
        numbers (list): 並び替える数値のリスト
    Returns:
        list: 並び替えた数値のリスト
    """ 
    for i in range(len(numbers)):
        for j in range(len(numbers) - 1):
            if numbers[j] > numbers[j + 1]:
                # swap
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j] # 交換
    return numbers # 並び替えたリストを返す

# 上記の関数のテスト
def test_bubble_sort():
    # テスト用のランダムなデータ
    import random
    nums = [random.randint(0, 1000) for _ in range(10)]
    # バブルソートの関数を呼び出す
    assert bubble_sort(nums) == sorted(nums)


# バブルソートの関数を呼び出す
if __name__ == '__main__':
    import random
    numbers = [random.randint(0, 1000) for _ in range(10)]
    print(numbers)
    bubble_sort(numbers)
    print(numbers)
    test_bubble_sort()