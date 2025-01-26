'''
Constructors in OOP's
A special method to initalize class attributes
Assert statement
'''

class Items:
    def __init__(self,name:str,price:int,quantity:int):
        
        '''
        Runs validations on recieved arguments using assert
        '''
        assert price>=0,f"Recieved {price} as negtive: , Expected ve+\nAssertionError{price} !>=0 "
        assert quantity>=0,f"Recieved {quantity} as negtive: , Expected ve+\nAssertionError{quantity} !>=0 "
        '''
        The parameters from __init__ we assigning them to object , usig typo
        '''
        self.name=name  
        self.price=price
        self.quantity=quantity

    def calculate_total_price(self,x,y):
        return x*y
    
    def calculate_total_price(self):
        return self.price*self.quantity

item=Items(name="lapptop",price=10000,quantity=-1)
print(item.name)

# total=item.calculate_total_price(item.price,item.quantity)
# print(total)
total1=item.calculate_total_price()
print(total1)
