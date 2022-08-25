a = [1, 2, 3]
b = [11, 12, 13]
c = []

if len(b)> len(a):
    for i in range(len(a)):
        c.append(a[i])
        c.append(b[i])
    for i in range(len(a),len(b)):
        c.append(b[i])
else:
    for i in range(len(b)):
        c.append(a[i])
        c.append(b[i])
    for i in range(len(b), len(a)):
        c.append(a[i])
print("c= ", c)

