import json

# 辞書型データ
data = {
    "no": 5,
    "code": ("jas", 1, 19),
    "scr": "be quick to listen, slow to speak, slow to anger",
}
# ファイルへ書き込む
filename = "test.json"
with open(filename, "w") as fp:
    json.dump(data, fp)

