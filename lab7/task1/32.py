n = int(input())
a = list(map(int, input().split()))
s = 0
for i in range(1,n):
    if(a[i - 1] < a[i]):
        s += 1

print(s)