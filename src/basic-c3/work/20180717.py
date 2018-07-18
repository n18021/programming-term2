# 今年度の放課後掃除当番と、給食当番！！
import random
# リストを入力しよう
menber1 = ["磯龍矢", "稲福裕哉", "仲宗根文也"]
me1 = random.randint(0, len(menber1)-1)

menber2 = ["川上大輔", "比嘉竜士", "川上浩介"]
me2 = random.randint(0, len(menber2)-1)

menber3 = ["椎名林檎", "斉藤由紀", "徳永英明"]
me3 = random.randint(0, len(menber3)-1)

# 選んだデータを表示しよう
fofo = "今年度の給食当番と、放課後掃除当番は,{0}君と{1}君と{2}さんに決定しました!!!おめでとうございます".format(menber1[me1],menber2[me2],menber3[me3])

print(fofo)
