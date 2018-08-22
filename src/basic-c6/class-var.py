class Cat:
    # クラス変数
    nakigoe = "nya-"
    # メソッド
    def naku(self):
        print(Cat.nakigoe)

mike = Cat()
mike.naku() # nya-

nora = Cat()
nora.naku() # nya0

# ここでクラス変数を変更する
Cat.nakigoe = "myu-"

# するとすべてのインスタンスで値が変更される
nora.naku()
mike.naku()
