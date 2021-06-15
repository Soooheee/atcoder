h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
sumh = [[0] for i in range(h)]
sumw = [[0] for j in range(w)]
print(sumh)
print(sumw)
for i in range(h):
    for j in range(w):
        print(a[i][j])
