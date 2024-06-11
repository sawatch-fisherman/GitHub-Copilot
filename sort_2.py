def bubble_sort(numbers):
    # ここに、バブルソートを実装する
    # バブルソートのアルゴリズム
    # 1. 隣り合う要素を比較する
    # 2. 前の要素が後ろの要素より大きければ、交換する
    # 3. すべての要素について 1. を実行する
    # 4. 1. の処理中に交換が行われなかったら、ソート終了
    for i in range(len(numbers)):
        for j in range(len(numbers) - 1):
            if numbers[j] > numbers[j + 1]:
                # swap
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

before = [5, 2, 4, 6, 1, 3]
print(before)
after = bubble_sort(before)
print(after)
