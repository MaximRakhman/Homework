count = 0
for i in range(2,101):
    count = 0
    for f in range(2,i):
        if i % f == 0:
            count = 1
    if count == 0:
        print(i)