# Taller Clase 15

Realizar una aplicación CRUD, aplicando el patrón MVC para la gestión de pedidos de mesa para el restaurante **EL CORRIENTAZO**.

El sistema debe tener las siguientes funcionalidades:
* Debe gestionar el número de mesa que hace el pedido (pueden ser varias mesas en el restaurante)
* En una mesa, pueden hacer varios pedidos (uno por cada persona que está en la mesa).
* Las opciones de pedido son:
  * Sopa
  * Principio
  * Carne
  * Ensalada (si o no)
  * Jugo
* Por cada opción de pedido, el cliente puede elegir entre varias opciones según el día que vaya a comer.
* Cuando el pedido de una mesa es entregado, este debe quedar marcado como pendiente de cobrar.
* Un cliente puede pedir algo adicional durante su estadía, por lo cual, lo que pida se agregará al pedido de la mesa.
* El sistema debe calcular el valor a pagar del pedido de la mesa.
* Cuando los clientes pagan lo consumido, y dejan el restaurante, se debe eliminar el pedido del sistema.