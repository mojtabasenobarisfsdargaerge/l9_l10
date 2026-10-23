'''
        /\
       /  \
      / M  \
     /      \
    _________
'''
class prodact:
    def __init__(self,name,price,quantity,category):
        self.name =name
        self.price =price
        self.quantity =quantity
        self.category =category
    def __str__(self):
        print(f"name ={self.name} price ={self.price} quantity ={self.quantity} category ={self.category}")
        def update_price(self,now_price):
            if now_price <0:
                raise ValueError("naw_price <0 nest")
            self.price =self.now_price
            print(f"mane be{self.price} tabdel shod")
        def add_stock(self,tedad):
            if tedad <1:
                raise ValueError("tedad pain 0 nemebashad")
            self.quantity += tedad
            print(f"tedad :{self.quantity}")
        def sell(self,tadad):
            self.quantity -= self.tedad
            print(f"tedad :self.quantity")
        def apply_discount(self,takhfef) :
            self.price * self.takhfef
        def total_value(self):
            r =self.quantity * self.price
            return r

