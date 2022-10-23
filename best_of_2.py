t=int(input('Enter number of test cases: '))
for i in range(t):
    X,Y=map(int,input().split())
    print(max(X,Y))