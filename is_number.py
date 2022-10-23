import re

for _ in range(int(input('Enter number of inputs: '))):
    print(bool(re.fullmatch("((?:\+|-)?\d*\.\d+)", input('Enter input: '))))
