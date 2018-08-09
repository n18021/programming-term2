# パッケージをインポート
import qrcode
# qrcodeを作成
img = qrcode.make("http://kujirahand.com/")
# ファイルに保存
img.save("qrcode-test.png")
