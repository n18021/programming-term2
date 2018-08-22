# クラスを設計したところ
class Human:
    '''人間を表すクラス'''
    def seach(self, place):
        '''周りを見る処理'''
        pass

    def take(self, food):
        '''ものをつかむ処理'''
        self.food = food

    def opan_mouth(self):
        '''口を開ける処理'''
        pass

    def eat(self):
        '''食べ物を食べる処理'''
        print(self.food + "を食べました。")


hito = Human()


hito.take("Banana")
hito.eat()
