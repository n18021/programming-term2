# テキストからキーワードを探す
key = "find"
with open("mt7_7.txt", encoding="utf-8") as tf:
    # 1行ずつ含む
    for i, line in enumerate(tf):
        # 文字列keyが行に含まれるか
        if line.find(key) >= 0:
            print(i + 1, ":", line)
