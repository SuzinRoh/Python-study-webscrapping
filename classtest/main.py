class Car():
    
    def __init__(self, *args, **kwargs):
        self.wheels = 4
        self.doors = 4
        self.windows = 4
        self.color = kwargs.get("color", "black")
        self.price = kwargs.get("price", "$20")
    
    def __str__(self):
       return f"Car with {self.wheels} wheels"
 
class  Convertible(Car):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.time = kwargs.get("time", 10)
    
    def take_off(self):
        return "taking off"   
    
    def __str__(self):
        return f"Car with no roofs"   
        

    

porche = Convertible(color="green", price="$40")
mini = Car()
porche.color = "red"
print(porche.color)