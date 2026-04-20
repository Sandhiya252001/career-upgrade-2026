class Product:
    productName="Mobile Phone"
    def __init__(self,price):
        self.price=price
        
    def priceDetails(self):
        return f"The price of the item is: {self.price}" 
    @classmethod
    def product(cls):
        return f"The ProductName is : {cls.productName}"
    @staticmethod
    def displayMethod():
        return f"Product details displayed"
p1=Product(30000)
print(p1.priceDetails())
print(Product.product())
print(Product.displayMethod())



    
        




