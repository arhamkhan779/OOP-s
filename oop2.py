'''
Methods initializations
Self Parameter inside method
'''
# class Items:
#     def calulate_total_price():
#         pass
    
# items=Items()
# price1=items.price=1000
# quantity1=items.quantity=10
# name1=items.name="bottle"
# items.calulate_total_price()

class Item:
    def calulate_total_price(self,x,y):
        return x*y
    
item1=Item()
item1.price=1000
item1.quantity=10
item1.name="bottle"
print(item1.calulate_total_price(item1.price,item1.quantity))
