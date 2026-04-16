class Perro:
 
    def __init__(self, raza= ""): 
       self.raza=raza
       self.edad=1

    def __str__(self):
        return f"{self.raza} de {self.edad} años"
    
    def ladrar(self):
      print (f" {self.raza} dice guau")


p =Perro()
print(p)
q =Perro("Firu")
print(q)
q.ladrar()


