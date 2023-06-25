x = [1, 2, 3, 4, 5]
y = ['a', 'b', 'c', 'd', 'e']
z = zip(x, y) # zip class
for item in zip(x, y):
    print(item)

# zip関数の返り値はアンパックできる
for item_x, item_y in zip(x, y):
    print(item_x, item_y)
