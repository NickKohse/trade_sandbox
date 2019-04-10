import time

class Transaction:
    def __init__(self, id, ticker, quantity, price, ttype, fee):
        self.time = time.ctime()
        self.id = id
        self.ticker = ticker
        self.quantity = quantity
        self.price = price
        self.ttype = ttype
        self.fee = fee
