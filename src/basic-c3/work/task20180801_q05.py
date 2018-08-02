# とある五人を年長順に並べるプログラム
arashi = {
    "Aiba": 35,
    "Matsumoto": 34,
    "Ninomiya": 35,
    "Oono": 37,
    "Sakurai": 36
}

# 年長順で並び替えて表示

li = sorted(
    arashi.items(),
    key=lambda x: x[1],
    reverse=True)
for name, age in li:
    print(name, age)
