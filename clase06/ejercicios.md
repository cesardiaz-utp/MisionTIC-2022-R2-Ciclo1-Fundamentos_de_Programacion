# Ejercicios Clase 6

## Condicionales

1. Diseñe un algoritmo que reciba una nota definitiva entre 0.0 y 5.0. El algoritmo debe imprimir el valor ingresado, y de ser una nota mayor o igual a 4.0, deberá imprimir un mensaje de felicitaciones.
1. Diseñe un algoritmo que reciba una nota definitiva entre 0.0 y 5.0. El algoritmo debe imprimir el valor ingresado, y un mensaje que indique si el estudiante “Ganó el curso” o “Perdió el curso”. Se gana el curso solo si la nota definitiva es mayor o igual a 3.0.
1. Diseñe un algoritmo que permita solicitar tanto el nombre como la edad de una persona y posteriormente indicar si es “Mayor de edad” o “Menor de edad” según la información ingresada. Una persona se considera mayor de edad si tiene 18 años o más.
1. Diseñe un algoritmo que determina si un número es par o impar. Recuerde que un número es par si el resto de una división entera con el número 2 es cero.
1. Diseñe un algoritmo que determine si un número real (x) se encuentra dentro del rango abierto-cerrado (3.5, 7.8].
1. Diseñe un algoritmo que determine si un número real (x) se encuentra dentro de uno de los siguientes rangos: (3.5, 7.8], [9.3, 4.5) y [23.4, 45.3].
1. Diseñe un algoritmo que permita imprimir un mensaje según un carácter dado por el usuario, independiente que sea ingresado en mayúscula o minúscula, según la Tabla:

| Carácter | Mensaje a imprimir |
|----------|--------------------|
|   'a'    | Android            |
|   'i'    | IOS                |
|   otro   | Opcion inválida    |

8. Diseñe un algoritmo que permita imprimir un mensaje según la nota definitiva de un estudiante entre 0.0 y 5.0, de acuerdo conla Tabla:

| nota     | Mensaje a imprimir |
|----------|--------------------|
|  < 3.0   | Insuficiente       |
|  <= 3.5  | Aceptable          |
|  <= 4.0  | Sobresaliente      |
|  <= 5.0  | Excelente          |

9. Diseñe un algoritmo que determine mayor número entre cuatro posibles números.
1. La oficina de aguas de la ciudad requiere crear un algoritmo que le permita liquidar las facturas de sus clientes durante cada mes. El cobro de cada factura se realiza de la siguiente forma: se cobra el cargo fijo, el consumo de agua en el periodo, es decir, la cantidad de metros consumidos y el servicio de recolección de basuras y alcantarillado. Construya un algoritmo que, al ingresarle es estrato socioeconomico del predio y la cantidad de metros cúbicos de agua consumidos, permita determinar el valor de la factura a pagar. Todos estos cobros se llevan a cabo dependiendo del estrato socioeconómico al que pertenezca el predio, de acuerdo con la siguiente tabla:

|Estrato|Cargo Fijo|Metro3 consumido|Basuras y alcantarillado|
|-------|-----|-----|------|
|1      |$2500|$2200|$5500 |
|2      |$2800|$2350|$6200 |
|3      |$3000|$2600|$7400 |
|4      |$3300|$3400|$8600 |
|5      |$3700|$3900|$9700 |
|6      |$4400|$4800|$11000|

11. La oficina de incorporación del ejército necesita un algoritmo que le pueda permitir saber si un aspirante a ingresar a la institución como soldado es apto o no para poder vincularlo. Para que una persona sea apta, debe cumplir los siguientes requisitos:
* Si es mujer, su estatura debe ser superior a 1.60 mts y su edad debe estar entre 20 y 25 años.
* Si el aspirante es hombre, se estatura debe ser superior a 1.65 mts y su edad debe estar entre los 18 y 24 años.

  Tanto mujeres como hombres deben ser solteros. Diseñe el algoritmo de tal forma que permita informar si un aspirante es apto o no para ingresar al ejercito.

## Diccionarios
Tres mejores amigos están en el autocine. En Autocinema Ukumarí, han patentado un sistema de servicio de gaseosas por botones, en el que se puede servir una cantidad predeterminada de gaseosa según el botón presionado. Cada uno de ellos tiene un vaso con una capacidad dada, y ya han llenado un cierto nivel del vaso. Como son mejores amigos, ellos quieren oprimir el mismo siguiente botón para servirse una cantidad fija de gaseosa en sus respectivos vasos. No obstante, no quieren que se les riegue la gaseosa, porque consideran que sería un desperdicio.  

Dadas la capacidad máxima de cada uno de los vasos, así como su capacidad actual, y el usuario al que pertenecen, escriba una función que determine el nombre de la persona a la que se le regaría algo de gaseosa, si se sirve la capacidad fija dada. Si a ninguno se le riega la gaseosa, retorne None. Si se le riega la gaseosa a más de uno, retorne el primero en orden de parámetros pasados a la función (es decir, primero llena el amigo 1, luego el 2, luego el 3).

**Nombre de la función**: desperdicio_de_gaseosa

**Parámetros**  
|Nombre|Tipo|Descripción|
|-------|-----|-----|
|amigo_1|dict|Un diccionario con las siguientes llaves: "nombre", el nombre del amigo, (str) "capacidad_vaso", la capacidad máxima de su vaso, (float) "capacidad_actual", la capacidad que ha sido llenada de su vaso hasta el momento (float)|
|amigo_2|dict|Un diccionario con las siguientes llaves: "nombre", el nombre del amigo, (str) "capacidad_vaso", la capacidad máxima de su vaso, (float) "capacidad_actual", la capacidad que ha sido llenada de su vaso hasta el momento (float)|
|amigo_3|dict|Un diccionario con las siguientes llaves: "nombre", el nombre del amigo, (str) "capacidad_vaso", la capacidad máxima de su vaso, (float) "capacidad_actual", la capacidad que ha sido llenada de su vaso hasta el momento (float)|
|capacidad_boton|float|La cantidad de gaseosa que se servirá si los amigos deciden oprimir el botón correspondiente.|

|Tipo del retorno|Descripción del retorno|
|-------|-----|
|str|El nombre del amigo a quien se le riega primero la gaseosa, suponiendo un orden ascendente en cuanto a que amigo llena primero su vaso. (Es decir, primero llena el amigo 1, luego el 2, luego el 3) Si a ningun amigo se le riega la gaseosa, retorne None. Si a más de un amigo se le riega la gaseosa, retorna el primero.|