# Ejercicios Clase 12

## List Comprehension

### Ejercicio 1
Necesitamos crear una lista de enteros que contenga la longitud de cada palabra en una frase, pero solo si la palabra no es "el".  
La frase es: `"el rápido zorro marrón salta sobre el perro perezoso"`

### Ejercicio 2
Crea una nueva lista que a partir de otra lista de números que contenga solo los números positivos de la lista, como enteros.  
La lista es `numeros = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]`

### Ejercicio 3
Extraiga en un conjunto los dígitos que existen en una frase. La frase es `"Hello 12345 World 5602"`

### Ejercicio 4
Que valores generan las siguientes List Comprehensions
* `[x**2 for x in range(10)]`
* `[2**i for i in range(13)]`

### Ejercicio 5
Cual sería la expresión List Comprehension para generar la siguiente lista: `[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]`

### Ejercicio 6
Con la lista `frutas = ['mango', 'kiwi', 'fresa', 'guayaba', 'piña', 'mandarina', 'uva', 'banano']`generar otra con la cantidad de caracteres que tiene cada fruta: `[5, 4, 5, ...]`.

### Ejercicio 7
Con la lista `frutas = ['mango', 'kiwi', 'fresa', 'guayaba', 'piña', 'mandarina', 'uva', 'banano']`generar otra con las frutas que solo tengan exactamente 2 vocales: `['mango', 'kiwi', ...]`.

### Ejercicio 8 - Especial 
Crear una lista con los números primos que existen entre el 2 y el 100.

## Funciones map(), reduce(), filter()
### Ejercicio 9
Usando las funciones map(), reduce(), filter()
```python
from functools import reduce 

# Utilice map() para imprimir el cuadrado de cada número redondeado
# a tres lugares decimales
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
map_result = list(map(lambda x: x, my_floats)) # Arreglar esta instrucción
print(map_result)

# Utilice filter() para imprimir solo los nombres que sean menores
# o iguales a siete letras
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
filter_result = list(filter(lambda name: name, my_names, my_names)) # Arreglar esta instrucción
print(filter_result)

# Utilice reduce() para imprimir el producto de estos números
my_numbers = [4, 6, 9, 23, 5]
reduce_result = reduce(lambda num1, num2: num1 * num2, my_numbers, 0) # Arreglar esta instrucción
print(reduce_result)
```

## Funciones all(), any()
### Ejercicio 10
Se recibe una lista de números enteros separados por espacios: Si todos los enteros son positivos, se debe revisar si algún entero es un número palíndromo como se muestra a continuación https://en.wikipedia.org/wiki/Palindromic_number. Se imprime la palabra ‘True’ si se cumplen las condiciones o ‘False’ de lo contrario.
Ejemplos:
* Para `[10, 30, 50, 90, 100, 101]` imprime `True`
* Para `[10, 20, 30, 400, 50, 100]` imprime `False`
* Para `[1, 2, 3, 4, 5, 6, 7, 8, 9]` imprime `True`
* Para `[151, 60, -5, 135, 18, 40]` imprime `False`