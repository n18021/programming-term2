#bmi判定プログラム
weight = float(int(input("体重（kg）は？"))
height = float(int(input("身長 (cm) は？"))
# bmi の計算
height  = height / 100 # m に戻す
bmi = weight = / (height * height)
# bmiの値に応じて結果を分岐
result = ""# 初期化
if bmi < 18.5:
    result = "痩せ型"
elif (18.5 <= bmi) and (bmi < 25):
    result = "標準体重"
elif (25 <= bmi) and (bmi < 30):
    result = "肥満(軽)"
elif bmi >= 30:
    result = "肥満（重）"
#結果を表示
print("BMI :", bmi)
print("判定:", result)
