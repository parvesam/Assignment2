class Month():
    def __init__(self, manufactured, sold, stock, cost, saleprice): #attributes
        self.manufactured = manufactured
        self.sold = sold
        self.stock = stock
        self.cost = cost
        self.saleprice = saleprice

    def __str__(self):
        return '\nManufactured: '+ str(self.manufactured)+ ' units ' +'\nSold: '+ str(self.sold)+ ' units '+ '\nStock:' + str(self.stock)+ ' units '

    def netProfit(self): #created class netProfit
        p = (self.sold*self.saleprice)-(self.manufactured*self.cost)
        return p
