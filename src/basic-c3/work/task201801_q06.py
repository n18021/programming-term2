# とある背の小さい順に並べるプログラム
arashi = {
    "Aiba": 175,
    "Matsumoto": 172,
    "Ninomiya": 168, 
    "Oono": 166,
    "Sakurai": 171 
}

# 年長順で並び替えて表示

li = sorted(
    arashi.items(),
    key=lambda x: x[1],
    reverse=False)
for name, age in li:
    print(name, age)
