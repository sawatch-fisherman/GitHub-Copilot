# fizz-buzz問題のコード
# 3の倍数の時はFizz、5の倍数の時はBuzz、15の倍数の時はFizzBuzzを出力する
# 1から100までの数字を出力する
# ただし、3と5の倍数の時は数字の代わりにFizz、Buzz、FizzBuzzを出力すること
# それ以外は数字を出力すること
# ただし、for文とif文を使用すること

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz') # 3と5の倍数の時はFizzBuzzを出力
    elif i % 5 == 0:
        print('Buzz') # 5の倍数の時はBuzzを出力
    elif i % 3 == 0:
        print('Fizz') # 3の倍数の時はFizzを出力
    else:
        print(i) # それ以外は数字を出力
    


