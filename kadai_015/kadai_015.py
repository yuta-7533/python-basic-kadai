#kadai_015

#Human classの作成
class Human:
    #コンストラクタの作成（名前、年齢）
    def __init__(self,name,age):
        self.name=name
        self.age=age

    #printinfoメソッドの作成
    def printinfo(self):
        print(self.name)
        print(self.age)

Jordan=Human("Jordan",26)
Jordan.printinfo()