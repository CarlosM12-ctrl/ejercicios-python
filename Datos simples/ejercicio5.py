#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
#Después debe mostrar por pantalla la paga que le corresponde.

ht = float(input("¿Cuántas horas trabajó?: "))#se crea un input con la variable flotante llamada ht 
ph = float(input("¿Cuánto equivale 1 hora trabajada?: "))#se crea otro input con la variable flotante llamda ph
print("Usted trabajó: ", ht, "Lo que equivale a: ", ht*ph)#se manda a imprimir el resultado con print y junto los valores ya calculados en el mismo print
#tambien puedes crear variables la cual almacenen la operacion "ht*hp"
