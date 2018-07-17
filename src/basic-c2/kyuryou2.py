#時給計算プログラム

#時給の入力ーー
user = input("時給はいくらですか？")
jikyu = int(user)

# 時間の入力
user = input("何時間働きましたか？")
jikan = float(user)

#　計算
kyuryou = jikan * jikan
# 結果を表示
fmt = """
時給は{0}円で、{1}時間働いたので、
時給は、{2}円です
"""
desc = fmt.format(jikyu, jikan, kyuryou)
print(desc)
