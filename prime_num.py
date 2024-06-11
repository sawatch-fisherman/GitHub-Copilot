# 1から100までの素数を表示するコード


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

for i in range(2, 101):
    if is_prime(i):
        print(i, end=' ')