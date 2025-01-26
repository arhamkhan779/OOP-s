'''
Using a magic method __repr__ to represent object differently
'''
import csv

class Items:
    all=[]
    discount=20

    def __init__(self,name:str,price:int,quantity:int):
        assert price>=0, f"Error Encountoured"
        assert quantity>=0, f"Error Encountoured"
        self.name=name
        self.price=price
        self.quantity=quantity

        Items.all.append(self)

    def __repr__(self):
        return f"Items({self.name},{self.price},{self.quantity})"
    
    def calculate_total_price(self):
        try:
            return self.price*self.quantity
        except Exception as e:
            raise e
    
    def apply_discount(self):
        try:
            self.price=self.price - ((self.price/100)*self.discount)
            return self.price
        except Exception as e:
            raise e
        
    @classmethod
    def instentiate_objects(cls):
        with open("data.csv",'r') as f:
            reader=csv.DictReader(f)
            items=list(reader)
        for item in items:
            Items(name=item.get("name"),price=int(item.get("price")),quantity=int(item.get("quantity")))
    
# item1=Items(name="laptop",quantity=20,price=2000)
# item2=Items(name="mouse",quantity=8,price=1000)
# item3=Items(name="keyboard",quantity=5,price=3000)
# item4=Items(name="printer",quantity=15,price=4000)
# item5=Items(name="earpods",quantity=10,price=5000)


Items.instentiate_objects()
print(Items.all)
