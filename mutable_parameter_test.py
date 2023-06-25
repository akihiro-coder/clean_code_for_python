# 仕様:関数の第一引数に与えた値をリスト化して返す
def f(value, list_obj=[]):
    list_obj.append(value)
    return list_obj


result_1 = f(value=1)  # [1]
result_2 = f(value=1)  # [1, 1]
print(id(result_1) == id(result_2))  # True 同じメモリ位置を参照


# 修正
def g(value, list_obj=None):
    if list_obj is None:
        list_obj = []
    list_obj.append(value)
    return list_obj

result_1 = g(value=1)  # [1]
result_2 = g(value=1)  # [1, 1]
print(result_1)
print(result_2)
print(id(result_1) == id(result_2))  # False 違うメモリ位置を参照
