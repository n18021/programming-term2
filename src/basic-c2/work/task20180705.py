#値段
sake_n = 200
tumami_n = 100
yakitori_n = 100

#個数
sake_k = 2
tumami_k = 1
yakitori_k = 2

#割引率
rate = (0.2) 
point = 150

#計算
kaikei = (sake_n * sake_k) + (tumami_n * tumami_k) + ((yakitori_n * yakitori_k) * (1 - rate)) - (point)

#結果
print("買い物の合計は", kaikei,"円です")
