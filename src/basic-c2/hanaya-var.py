#花屋の支払いの金額を求める
#値段
rose_v = 500
sun_v = 400
tulip_v = 700
#個数
rose_c = 18
sun_c = 8 - 2
tulip_c = 21-5
#割引率
rate = 0.1
#計算
sun_v = (rose_v * rose_c) + (sun_v * sun_c) + (tulip_v * tulip_c)
payment = sum_v * rate
#結果表示
print("買い物の合計は",sum_v, "円")
print("割引してもらうと", payment, "円")

