# 関数の外側でvalueに100を代入
value = 100

def changeValue():

    """
    値を変更

    parameters
    -----------
    なし

    returns
    -----------
    なし
    """
    # 関数の内側でvalueを変更
    value = 20


changeValue()
print("value=",value) # <--果たしてこの値は？
