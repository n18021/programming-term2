# 印税を計算する関数
def calc_royalty(price, sales, per):
    rate = per / 100
    ro = int(price * sales * rate)
    return ro

# ユーザーから情報を入力してもらう
i = int(input("定価は？"))
price = int(i)

i = input("発行部数は？")
seles = int(i)

i = input("印税率は（%）")
per = float(i)

# 結果を表示する
v = calc_royalty(price, seles, per)
print("印税は、", v, "円です")
