# 辞書型のデータ（果物名と値段）を変数に代入
fruits = {
    "バナナ": 300, "イチゴ": 350,
    "オレンジ": 240, "マンゴー": 400}

# 辞書型のデータ一覧を表示
for name, price in fruits.items(): # ---------
    # 画面に出力
    s = "{0}は、{1}円です。".format(name, price)
    print(s)
