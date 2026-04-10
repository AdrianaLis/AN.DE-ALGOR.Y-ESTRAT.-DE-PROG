""""
 Pida el nombre del cliente,
 Cuantas manzanas comprara y un precio.
 Muestre el nombre y el total a pagar
 """
print("Ingrese nombre ")
nom=input()
print ("Ingrese el nro de manzanas que compro")
cant = int(input())
print( "Ingrese el precio de las manzanas")
prod=float(input())

print(f"Su nombre es: {nom} y compro {cant}  manzanas por lo cual pago: {cant*prod}")
print()

nom=input ("Ingrese nmobre: \n")
can= int (input("Ingrese cantidad manzanas: \n"))
pre=float (input("Ingrese precio:\n "))
tot= can * pre
print (f"{nom} compro $ {tot}")
