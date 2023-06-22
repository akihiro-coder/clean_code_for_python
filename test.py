# unpack 複数の値を複数の変数に割り当てることができる
x, y = 1, 2
print(x, y)

# これを応用したのが下の例
x = [1, 2, 3, 4, 5]
a, b, c, d, e = x
print(a, b, c, d, e)
A, B, *C = x  # *印をつけてまとめて押し込む
print(A, B, C)

y = (1, 2, 3, 4, 5)  # タプルもいける
a, b, c, d, e = y
print(a, b, c, d, e)

x, y, z = 2, 2, 2
print(x, y, z)
x = y = z = 2  # こんな書き方もできる
print(x, y, z)


# chane if sentence
x = 4
print(x >= 2 and x <= 8)
print(2 <= x <= 8)  # こっちのほうが見やすい


# None
x, y = 2, None
print(x == None)
print(y == None)
print(x is None)  # こんな書き方もできる
print(y is None)


# シーケンスと連想配列の繰り返し
x = [1, 2, 3, 4, 5]
for item in x:
    print(item)
for item in x[::-1]:  # こんな書き方があるが、、、
    print(item)
for item in reversed(x):  # このほうが可読性が高まる
    print(item)

# シーケンスの要素と対応するインデックスの両方が必要になるケース
for i in range(len(x)):  # なんとなく読みづらい
    print(i, x[i])
for i, item in enumerate(x):  # こっちのほうがスッキリしてみえる
    print(i, item)

# 2つ以上のシーケンスを反復処理したい場合
y = 'abcde'
for i in range(len(x)):  # なんだかダサい　読みづらい気も
    print(x[i], y[i])
for item in zip(x, y):  # スッキリ　「対となるタプルを返す」 アンパックと組み合わせると次のような書き方もできる
    print(item)
for x_item, y_item in zip(x, y):  # イケてる
    print(x_item, y_item)

# 辞書の反復処理
z = {'a': 0, 'b': 1}  # なんだか読みづらい
for key in z:
    print(key, z[key])
for key, value in z.items():  # スッキリしている
    print(key, value)
# おまけ
print(z.keys())
print(z.values())
print(z.items())


# 0との比較
x = (0, 1, 2, 3, 4, 5)
#①
for item in x:
    if item != 0: # スタンダードな書き方
        print(item)
#②
for item in x:
    if item: # 0はFalseとみなされる # しかしこの書き方には注意点もあり
        print(item)
y = (0, 1, 2, 3, 4, 5, [], '')
for item in y:
    if item:
        print(item) # 空リスト, 空文字列もFalseとみなされてしまう
        # 仕様が「0以外なら表示する」だと、「空リストや空文字列」が表示されないのは仕様違反となる 
        # 一方で① の書き方では、itemには数値が入っていると明示でき、コードの説明になっている



# ミュータブルなオプション引数(デフォルト引数)を避ける
def f(value, seq=[]):
    seq.append(value)
    return seq

# どんどん増えてしまっている！！！！！！！
print(f(value=1)) # [1]
print(f(value=2)) # [1,2]
print(f(value=3)) # [1,2,3] # オプション引数の同じインスタンスが、関数が呼び出されるたびに使われている


# 解決策
def f(value, seq=None):
    if seq is None:
        seq = []
    seq.append(value)
    return seq

print(f(value=1)) # [1]
print(f(value=2)) # [2]
print(f(value=3)) # [3]




# コンテキストマネージャーを使用してリソースを解放する
# my_file = open('test.jpg', 'w')
# my_file.close()

# with open('./test.jpg', 'w') as my_file:
#     # withブロックを使用することで、特殊メソッドの.__enter()__, .__exit()__が例外が発生した場合でも呼び出される
