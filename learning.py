# Pythonの基本を学ぶためのコード例です。

# 1. 変数の定義と基本的な型
# 整数型
number = 10
# 浮動小数点型
float_number = 10.5
# 文字列型
text = "Hello, Python!"

# 2. リスト
# リストの定義
my_list = [1, 2, 3, 4, 5]
# リストから要素を取得
first_element = my_list[0]  # 最初の要素
last_element = my_list[-1]  # 最後の要素

# 3. 条件分岐
# if文を使った条件分岐
if number > 5:
    print("numberは5より大きいです。")
else:
    print("numberは5以下です。")

# 4. ループ
# forループでリストの要素を一つずつ処理
for item in my_list:
    print(item)

# whileループで条件がTrueの間、繰り返し処理
count = 0
while count < 5:
    print(f"count = {count}")
    count += 1  # countを1増やす

# 5. 関数
# 関数の定義と呼び出し
def add(a, b):
    return a + b

# add関数を使って2と3を足す
result = add(2, 3)
print(f"2 + 3 = {result}")

# このコードはPythonの基本的な概念を紹介するもので、変数の定義、リストの操作、
# 条件分岐、ループ、関数の定義と呼び出しについて学ぶことができます。