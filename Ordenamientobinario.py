def busqueda_binaria(lista,objetivo):
  lower = 0
  higher= len(lista)-1
  while lower+1<higher:
      middle = (lower+higher)//2
      if lista[middle]==objetivo:
         return True
      elif lista[middle]< objetivo:
         lower = middle
      elif lista[middle]> objetivo:
         higher = middle

      return False

numeros=[4,5,10,15,20,25,30,35,40,45,50,58,65,80,98]
buscar=int(input("Ingrese numero a buscar"))
if busqueda_binaria(numeros,buscar):
   print (f"Numero encontrado")
else:
   print ("Número no encontrado")
   
      

