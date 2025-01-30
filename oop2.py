# '''
# Methods initializations
# Self Parameter inside method
# '''
# class Items:
#     def calulate_total_price(self):
#         print(self.name,self.price,self.quantity, self.color)
        
    
# items=Items()
# items.price=1000
# items.quantity=10
# items.color="black"
# items.name="bottle"

# items.calulate_total_price()

# items1=Items()
# items1.price=10000
# items1.quantity=100
# items1.name="laptop"
# items1.calulate_total_price()

# class Item:
#     def calulate_total_price(self,x,y):
#         return x*y
    
# item1=Item()
# item1.price=1000
# item1.quantity=10
# item1.name="bottle"
# print(item1.calulate_total_price(item1.price,item1.quantity))

class Items:
    def __init__(self,name:str,price:int,quantity:int):

        self.name=name
        self.price=price
        self.quantity=quantity
    
    def calculate_price(self):
        return self.price*self.quantity

item1=Items(name="laptop",price=2000,quantity=10)
item2=Items(name="laptop",price=4000,quantity=10)
item3=Items(name="laptop",price=3000,quantity=10)
item4=Items(name="laptop",price=5000,quantity=10)
item5=Items(name="laptop",price=1000,quantity=10)

print(item1.calculate_price())
print(item2.calculate_price())
print(item3.calculate_price())
print(item4.calculate_price())
print(item5.calculate_price())

