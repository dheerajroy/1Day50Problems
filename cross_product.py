from itertools import product
a, b = map(int, input().split()), map(int, input().split())
[print(i, end=' ') for i in product(a, b)]