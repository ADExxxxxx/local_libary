key = input().lower()
st = input().lower().split()

count = 0
pos = 0
min_pos = 0
flag = 0
flag2 = 0
for i in range(len(st)):
    if st[i] == key:
        count = count + 1
        if i == 0:
            flag2 = 1
        if flag == 0:
            min_pos = pos
            flag = 1
    else:
        pos = pos + len(st[i]) + 1
if count == 0:
    print(-1)
elif flag2 == 1:
    print(count, 0)
else:
    print(count, min_pos)