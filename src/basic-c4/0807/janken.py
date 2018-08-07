# じゃんけんゲーム
import random

# 手をリストで表現
hand = ["グー", "チョキ", "パー"]

print("===じゃんけんしましょう！===")
while True:
    # コンピュータの手を決定
    com = random.randint(0, 2)
    # ユーザーの手を入力してもらう
    for i ,desc in enumerate(hand):
        print(i, ":", desc)
   try:
    you = int(input("出す手を数値で入力"))
    if you == 3: break
    if you < 0 or you > 2:
        print("0から3までを入力してね")
        continue
   except:
        print("整数で入力してね")
    # 手を表示
    print("---")
    print("自分:", hand[you])
    print("相手:", hand[com])
    input("---")
    # じゃんけんの勝敗を判定する
    j = (you - com + 3) % 3
    if j == 0:
        print("あいこ")
    elif j == 1:
        print("負け(ToT)")
    else:
        print("勝ち")
    input("---")
