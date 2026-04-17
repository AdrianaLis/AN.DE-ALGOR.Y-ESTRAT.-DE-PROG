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

class Persona:  
    def __init__(self):
        self.nombre_usuario= input ("Ingrese nombre\n")
        self.edad_usuario=int(input("Ingrese edad\n"))

           
    def mostrar(self):
       print(f" Mi nombre es :{self.nombre_usuario} y tengo :{self.edad_usuario} años")
    
def menu():
       usuario= None
       while True:
          print( "-----Menú------")
          print("1.Ingresar datos")
          print("2.Ver datos")
          print ("3.Salir")
          opcion= input(" Seleccione su opcion:")
          if opcion=="1":
             usuario = Persona()
             print("Persona registrada con exito")
          elif opcion=="2":
             if usuario:
                usuario.mostrar()
             else: print("Errooor  Debe ingresar sus datos")
          elif opcion=="3":
             print("Saliendo del programa")
             break
          else: print("Opcion no valida")

   
menu()

             

       











