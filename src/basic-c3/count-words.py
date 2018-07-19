# 単語の出現回数をカウント
text = """
keep on asking, and it will be given you;
keep on seeking, and you will find;
keep on knocking, and it will be opened to you;
for everyone asking receives, and everyone seeking finds,
and to everyone knocking, it will be opened.
"""

# 単語を切る
text = text.replace(";", "")  # ; を削除
text = text.replace(",", "")
text = text.replace(".", "")
words = text.split()  # 空白で区切ってリスト型を作成

# 単語を数える
counter = {} # counter と言う空の辞書型を作成
for w in words:
    ws = w.lower()  # 少文字に変換
    if ws in counter:  # もし辞書型にすでにキーがあれば値を一つ追加
        counter[ws] += 1
    else:
        counter[ws] = 1
# 結果を表示
for k,v in sorted(counter.items()):  # counter のキーをアルファベット順として範囲に指定
    if v >= 3:
         print(k,v)
