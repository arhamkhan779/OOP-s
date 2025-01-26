class Items:
    discount=20

    def __init__(self,name:str,price:int,quantity:int):
        assert price >=0, f"Error got -ve expected +ve"
        assert quantity >=0, f"Error got -ve expected +ve"

        self.name=name
        self.price=price
        self.quantity=quantity

    def calculate_price(self):
        try:
           return self.price * self.quantity
        except Exception as e:
            raise e    
        
    def apply_absolute_discount(self):

        '''
        It will apply discount that is predefine in our store
        '''
        self.price=self.price-(self.price/100)*Items.discount
        return self.price
    
    def apply_discount_on_certain_objects(self):

        '''
        This is the discount we can apply on certain products
        '''
        self.price=self.price-(self.price/100)*self.discount
        return self.price
    

item1=Items(name="laptop",price=4500,quantity=10)
item2=Items(name="laptop",price=4500,quantity=10)
item2.discount=30
item2.apply_discount_on_certain_objects()
item1.apply_absolute_discount()

print(item2.price,item1.price)



'''
we can update class level variable values using class name
and instance level variable by instance name
and instance both

if we access clas attributes via class names so they directly go to the class attributes
but if we access it thorugh instance level than first it finds it inside object , if not then it will get the class level attributes
'''

#checking all the attributes of class and objects
# print(item1.__dict__)
# print(Items.__dict__)
