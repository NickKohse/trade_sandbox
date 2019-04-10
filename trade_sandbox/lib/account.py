import constant
import api_connector
import exceptions
import asset
import transaction

class Account:
    def __init__(self, name, bal=constant.BALANCE, fee=constant.FEE):
        self.name = name
        self.balance = bal
        self.fee = fee
        self.asset_list = {}
        self.transactions = []
    
    def buy_asset(self, ticker, id, quantity):
        ai = api_connector.API_Connector()
        price = ai.get_price(id)

        if ((price * quantity) + self.fee) > self.balance:
            raise exceptions.FundsError((price * quantity) + self.fee, self.balance)
        
        if id in self.asset_list:
            self.asset_list[id].grow(price, quantity, self.fee)
        else:
            self.asset_list[id] = asset.Asset(quantity, ticker, id, price, self.fee)
        
        self.balance -= (quantity * price) + self.fee
        self.transactions.append(transaction.Transaction(id, ticker, quantity, price, "purchase", self.fee))
    
    def sell_asset(self, ticker, id, quantity):
        if id in self.asset_list:
            ai = api_connector.API_Connector()
            price = ai.get_price(id)

            if quantity > self.asset_list[id].quantity:
                raise exceptions.InsufficientHoldingsError(ticker, self.asset_list[id].quantity, quantity)
            elif quantity == self.asset_list[id].quantity:
                del self.asset_list[id]
            else:
                self.asset_list[id].shrink(quantity, self.fee)
                
            self.balance += (price * quantity) - self.fee           
        else:
            raise exceptions.AssetNotOwnedError(ticker)
        self.transactions.append(transaction.Transaction(id, ticker, quantity, price, "sell", self.fee))




