# 再帰関数を提示
"""
関数を表示
paramerers
==========
i : int  回数
return  無し
"""
def say_hello(i):
    if i <= 0:
         return
    print("ハロー", i)
    say_hello(i-1)

say_hello(10)
