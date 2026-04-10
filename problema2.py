"""
 Pide nombre y dni de un cliente y cree una función que valide que tenga 11 cifras tal que si falla le indique al usuario que esta mal escrito

  """

def validar_ruc(dato):
 if len(dato) == 11:
        return "Ruc correcto"
 else:
        return "Los datos ingresados son erroneos debe tener 11 cifras "

nom=input ("Ingrese nombre: \n")
can=input("Ingrese DNI: \n")
ruc=input("Ingrese Ruc: \n")
resultado = validar_ruc(ruc)
print(f"Cliente: {nom} y su dni es {can}")
print(resultado)
