'''
Saving objects in all list
'''

class Items:
    discount=20
    all=[]
    def __init__(self,name:str,price:int,quantity:int):
        assert quantity>=0, f"Error Encountoured"
        assert price>=0, f"Error Encountoured"
        
        self.name=name
        self.price=price
        self.quantity=quantity
        Items.all.append(self)

item1=Items(name="laptop",quantity=20,price=2000)
item2=Items(name="mouse",quantity=8,price=1000)
item3=Items(name="keyboard",quantity=5,price=3000)
item4=Items(name="printer",quantity=15,price=4000)
item5=Items(name="earpods",quantity=10,price=5000)

for elements in Items.all:
    print(elements.name,elements.price,elements.quantity)
        