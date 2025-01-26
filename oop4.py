'''
Class Level variables , class attributes acccess across all objects
Class Level variable can be accessed through classes and instances
If we are accessing class level variable through class name so it directly access class variables
but if we are accessing thorugh instances then , firstly python interpreter check whether the attribute present in object , if not then it willl retrieve class atributes
'''
class Items:
    discount=20
    name="arham"

    def __init__(self,name:str,price:int,quantity:int):

        assert price>=0, f"Erorr Expected +ve got -ve"
        assert quantity>=0, f"Erorr Expected +ve got -ve"
        self.price=price
        self.name=name
        self.quantity=quantity
    
    def calulate_price(self:object) ->int:
        return self.price*self.quantity
    
    def apply_discount(self:object) ->int:
        return self.price-((self.price/100)*Items.discount)



    
item1=Items(name="laptop",price=45,quantity=100)
item2=Items(name="CPU",price=1000,quantity=10)
print(item1.name)
print(item2.name)
print(Items.discount)
print(item1.discount)
print(item2.discount)