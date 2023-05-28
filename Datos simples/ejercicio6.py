#Escribir un programa que lea un entero positivo, n, 
#introducido por el usuario y después muestre en pantalla la suma 
#de todos los enteros desde 1 hasta n La suma de los n primeros 
#enteros positivos puede ser calculada de la siguiente forma: imagen2
n = int(input("dame un número: "))#declaramos el valor que se va a ingresar como entero
suma = n*(n+1)/2 #se realiza la operación
print("la suma de todos los numeros enteros desde 1 hasta", str(n), " es ", str(suma))#al resultado le ponemos str() para darle formato como cadena de texto
# En Python, la función str() se utiliza para convertir un valor a su representación en 
# formato de cadena (string). Esto es necesario cuando deseas concatenar un valor de otro tipo, 
# como un entero o un número de punto flotante, con una cadena en una operación de impresión.
# Si no utilizas str() en este caso, obtendrías un error de tipo, ya que no se puede concatenar 
# directamente un entero con una cadena.