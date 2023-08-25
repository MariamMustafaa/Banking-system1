class Bank:
    def __init__(self,acountnumber,amount,money):
        self.acountnumber=acountnumber
        self.amount=amount
        self.money=money

    def wihtdraw(self):
        if self.amount<self.money:
            print("The balance is not enough")
        else:
            self.amount-=self.money

    def deposit(self):
        self.amount+=self.money

    def transfer(self):
        if self.amount<self.money:
            print("The balance is not enough")
            # TODO 
bank=Bank("122344","30","10")
bank.wihtdraw()

