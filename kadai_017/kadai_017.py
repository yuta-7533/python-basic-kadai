#Human classの作成
class Human:
    #コンストラクタの作成（名前、年齢）
    def __init__(self,name,age):
        self.name=name
        self.age=age

    #check_adultメソッドの作成
    def check_adult(self):
        if self.age>=20:
              print(f"{self.name}は大人です。")
        else:
             print(f"{self.name}は大人じゃないです。")

Jordan=Human("Jordan",26)
Ema=Human("Ema",19)
Tom=Human("Tom",20)
Wendy=Human("Wendy",21)

list=[]
list.append(Jordan)
list.append(Ema)
list.append(Tom)
list.append(Wendy)

for i in range(len(list)):
     list[i].check_adult()