list_obj = [1,2,3]
var1, var2, var3 = list_obj # アンパック：コレクションの要素を一括して変数に代入する方法
                            # アンパック代入する際は、右辺のコレクションの要素数と、左辺に指定する変数の数が一致する必要がある
print(var1, var2, var3)

tuple_obj = (1,2,3)
var1, var2, var3 = tuple_obj # タプルでもアンパックは有効
print(var1, var2, var3)

str_obj = 'abc'
var1, var2, var3 = str_obj # 文字列を代入すると、1文字ずつ分割して代入される
print(var1, var2, var3)


list_obj = [1,2,3]
var1, *var2 = list_obj # 左辺の一部の変数にコレクションの要素を押し込むことができる
print(var1, var2)
