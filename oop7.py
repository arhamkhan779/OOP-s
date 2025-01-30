'''
Using a magic method __repr__ to represent object differently

instance variables : object attribute ,  
    ---accessibility -> can be access through only instances 
        - if inside class -> access via self
        - if outside class -> access via object name
        - cannot access inside class methods
        - can access inside instance methods

instance methods: object methods
    --- define inside class , take self(object) as first arguments
    ---accessibility -> instance methods can be access only thorugh objects
        - if inside class -> access via self
        - if outside class -> access via object name
        - cannot access inside class methods
        - can access inside instance methods

class variables: class attribute
    ---accessibility -> can be access through instance and class refrence
         - if access through class it will directly access the class variables
         - if access through instance , interpreter first find it in instance that present 
         - if not present it will access class level variable value
         - can access inside class methods and instance methods boths

class methods: class methods
    --- accessibility -> can access through instance and class names
         - if access thorugh class it will directly access the class method
         - if access thorugh instance it will first find it in instance scope
         - if not present it will access class level method
         - can access inside class methods as well as instance methods
        
    
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
            return self.price*self.quantity  # instance variable accessing inside instance methods via self
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
        # self.price ----> instance attributes cannot be access inside class methods
        with open("data.csv",'r') as f:
            reader=csv.DictReader(f)
            items=list(reader)
            
        for item in items:
            Items(name=item.get("name"),price=float(item.get("price")),quantity=int(item.get("quantity")))

    
    

item1=Items(name="laptop",price=100000,quantity=100)
item1.calculate_total_price()
# item1.instentiate_objects()

# Items.instentiate_objects()
print(Items.all)

Items.apply_discount()
