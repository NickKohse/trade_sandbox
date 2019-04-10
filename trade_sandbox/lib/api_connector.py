import constant

class API_Connector:
    def __init__(self):
        self.url = constant.URL
    
    def get_price(self, id):
        #return price of item
        return 6