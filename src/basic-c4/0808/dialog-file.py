# ダイアログを表示するために必要なモジュール
import tkinter.filedialog as fd

# ファイルを選択してダイアログで表示する
path = fd.askopenfilename(
    title="処理対象のファイルを指定してください"
)
print(path)
