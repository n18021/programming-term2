# 尺かCMまでの単位の変換
def syaku_to_cm(syaku):
    return round(syaku * 30.303, 3)

print(__name__)
if __name__ == '__main__':
    print(syaku_to_cm(30))
