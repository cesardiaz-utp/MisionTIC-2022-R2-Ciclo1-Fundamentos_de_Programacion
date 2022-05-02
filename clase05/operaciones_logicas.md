# Operaciones lógicas

Son tres las operaciones básicas del álgebra Booleana. El resto de operaciones, como la implicación o la equivalencia, son operaciones secundarias que se pueden construir a partir de la conjunción, disyunción y negación.

* **Negación**. La negación (¬, not, no) es la operación Booleana que toma un valor de verdad y lo convierte en el otro valor. Es decir que la negación de un valor verdadero es un valor falso, y la negación de un valor falso es un valor verdadero. La negación es una operación unaria, que se aplica sobre un solo operando.
* **Conjunción**. La conjunción (∧, and, y) es una operación Booleana binaria que tiene valor verdadero sólo cuando ambos operandos tienen valor verdadero. Esto implica que cuando un operando es verdadero y el otro es falso, o cuando ambos operandos son falsos, el resultado de una conjunción es un valor falso.
* **Disyunción**. La disyunción (∨, or, o) es una operación Booleana binaria que tiene valor verdadero cuando por lo menos uno de los operandos tiene valor verdadero. Esto implica que una disyunción tiene valor falso sólo cuando ambos operandos tienen valor falso.

## Probando las operaciones
**p**: Hoy está haciendo frio  
**q**: Hoy es lunes  
**r**: Hoy es un día de hacer deporte

```
q :      ________________________  
¬p :     ________________________
¬q :     ________________________
p ∧ q :  ________________________
p ∧ ¬r : ________________________
p v r :  ________________________
_____ :  Hoy es lunes u hoy es un dia de hacer deporte.
_____ :  Hoy no está haciendo frio y hoy no es dia de hacer deporte.
_____ :  Hoy es lunes y hoy es lunes.
_____ :  Hoy es lunes y hoy no es lunes.
_____ :  Hoy está haciendo frio y (hoy es lunes u hoy es un dia de hacer deporte).
_____ :  (Hoy está haciendo frio u hoy es lunes) y hoy es un dia de hacer deporte. 
_____ :  (Hoy está haciendo frio y hoy no es dia de hacer deporte) u (hoy no está haciendo frio y hoy es un dia de hacer deporte). 
```