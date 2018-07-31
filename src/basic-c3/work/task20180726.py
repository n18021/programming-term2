import random
print("ゴールは１０です。")
def shake_dice():
    return random.randint(1, 6)
"""
Parameters
----------
無し

Return
----------
random.randint(1,6)

1~6までのランダムな数
"""

def go_forward():
    return sum

"""
Parameters
-----------
無し

Return
----------
sum

sum関数で合計した値
"""
rist = []
while True:
    x = input("サイコロを振ってください。") 
    if x == "":
        rist.append(shake_dice())
        if go_forward()(rist) >= 10:
            print("{}が出ました。　おめでとうございます。ゴールしました。".format(shake_dice()))
            exit()
        else:
           print("{}がでました。現在位置は{}です。".format(shake_dice(),sum(rist))) 
