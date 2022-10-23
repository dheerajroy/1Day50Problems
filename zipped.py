nvals, n = map(int, input().split())
smarks = []
for i in range(n):
    smarks.append(list(map(float, input().split())))

[print(sum(i)/len(i)) for i in zip(*smarks)]
