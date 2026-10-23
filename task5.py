'''
        /\
       /  \
      / M  \
     /      \
    _________
'''
class bankaccount:
    def __init__(self,owner,account_namber,balanse):
        self.name =owner
        self.rmz_poya =account_namber
        self.price =balanse
        self.transactions =[]
    def __str__(self):
        print(f"name :{self.name} rmz_poya :{self.rmz_poya} price :{self.price} transaction :{self.transactions}")
    def deposet(self,mghdar =1000):
        if mghdar <0:
            raise ValueError(">0")
        self.price += mghdar
        self.transactions.append(f"+{self.price}")
    def 	withdraw(self,mghdar):
        if mghdar >self.price:
            raise ValueError("mghdar < price")
        self.price -=mghdar
        self.transactions.append(f"-{self.price}")
    def transfer(self, nam_carbare, mghdar):
        if nam_carbare.price <mghdar:
            raise ValueError("???")
        nam_carbare.price -= mghdar
        self.price          += mghdar
        nam_carbare.transactions.append(f"-{mghdar}")
        self.transactions.append(f"+{mghdar}")
    def 	get_balance(self):
        print(f"price ={self.price}")
    def	transaction_history(self,mod="classic"):
        if mod =="classic":
            print("______________________________")
            print("____transactions____")
            for t in self.transactions:
                print(t)
                print("_____________")  
        elif mod=="vip":
            self.price -=1000
            self.transactions.append(f"-{1000}")
            print("*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*")
            print("*_*_*_*_*_*_*_*_*transactions*_*_*_*_*_*_*_*_*")
            for t in self.transactions:
                print(t)
                print("*_*_*_*_*_*_*_*")
        elif mod=="star":
            print("************************************")
            print("*****************transactions*******************")
            for t in self.transactions:
                print(t)
                print("*****************")
        elif mod=="old":
            print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
            print("/\/\/\/\/\/transactions/\/\/\/\/\/")
            for t in self.transactions:
                print(t)
                print("/\/\/\/\/\/\/")
        elif mod=="vippass":
            self.price -=40404040
            self.transactions.append(f"-{40404040}")
            print("/\*\/*/\*\/*/\*\/*/\*\/*")
            print("/\*/\*\/*\/*\/transactions/\*/\*/*\/*\/*\/")
            for t in self.transactions:
                print(t)
                print("/\*/*\/*\/*\/*\*/\/")
        elif mod=="01":
            print('09320950228044854847634689873687732789')
            print("093485730925790759transactions34845372899750379930")
            for t in self.transactions:
                print(t)
                import random
                print(random.randint(10000000000,900000000000000))
        else:
            raise ValueError("in mod vogod nadarad")
            
            
ali = bankaccount("Ali", "1001", 5000000)
sara = bankaccount("Sara", "1002", 2000000)
ali.deposet(1000000)
ali.withdraw(500000)
sara.deposet(50000000)
ali.transfer(sara, 2000000)

sara.__str__()
ali.__str__()

ali.transaction_history()
ali.get_balance()
sara.get_balance()        
            
            
            
            
            
            
            