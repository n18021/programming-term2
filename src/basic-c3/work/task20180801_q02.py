# 消費税計算プログラム
shouhi = [13600, 14500, 16000, 111111, 11667]

TAX_RATE = 10 

zei = lambda x: round(x * (1 + TAX_RATE / 100))
print(list(map(zei, shouhi)))

