class Human:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        print(f"Привіт, {self.name}!")

    @classmethod
    def species_info(cls):
        return "Цей вид називається Homosapiens."
    
    @staticmethod
    def random_message():
        return "Це випадкове повідомлення."


person1 = Human("Олексій")
person2 = Human("Марія")

person1.greet() 
person2.greet()  

print(Human.species_info())  

print(Human.random_message())  
