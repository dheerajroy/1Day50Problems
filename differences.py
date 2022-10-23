m = int(input('Enter M: ')); mset = set(map(int, input().split()))
n = int(input('Enter N: ')); nset = set(map(int, input().split()))

[print(i) for i in sorted(list(mset.difference(nset)) + list(nset.difference(mset)))]