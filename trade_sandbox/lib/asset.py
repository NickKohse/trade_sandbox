class Asset:
    def __init__(self, quantity, ticker, id, price, fee):
        self.quantity = quantity
        self.ticker = ticker
        self.id = id
        self.price = price
        self.book_value = (quantity * price) + fee

    ##
    # Increase the quantity of an asset owned and update values accordingly
    # ARG - price: the price at which the additional shares will be purchased
    # ARG - quantity: the number of additional shares to be purchased
    # ARG - fee: the commission fee charged on this transaction
    # RETURN - nothing
    ##
    def grow(self, price, qunatity, fee):
        self.quantity += qunatity
        self.book_value += (price * qunatity) + fee
        self.price = self.book_value / self.quantity

    ##
    # Decreases the quantity of an asset owned and update values accordingly
    # ARG - quantity: the number of shares to be sold
    # ARG - fee: the commission fee charged on this transaction
    # RETURN - nothing
    ##
    def shrink(self, quantity, fee):
        self.quantity -= quantity
        self.book_value = (self.price * self.quantity) + fee
        

