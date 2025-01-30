class Items:
    #class variables

    discount=20
    def __init__(self,name,price,quantity):

        #Instance variables
        self.name=name
        self.price=price
        self.quantity=quantity
    
    #Instance mathods
    def calculate_price(self):
        return self.price*self.quantity #self (accessibility)
    
    

    
    #class method
    @classmethod
    def Is_integer(cls):
        Items.discount,cls.discount
        return isinstance(cls.discount,int)
    



item1=Items(name="laptop",price=2000,quantity=10)
item2=Items(name="mouse",price=3000,quantity=20)


 #OUTSIDE CLASS
    