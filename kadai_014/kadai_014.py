#kadai_014
price1 = 100
price2 = 200
tax = 1.1

def total():
    #下記のtaxオブジェクトはローカル変数
    #よってローカルスコープ内のみ有効
    #グローバルスコープの4行目に移動した
    #tax = 1.1
    return price1 + price2

print (total() * tax)
