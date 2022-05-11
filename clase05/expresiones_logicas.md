# Tablas de verdad

## Tabla de verdad de la **negación**
| p |  ¬p |
|---|-----|
| T |  F  |
| F |  T  |

## Tabla de verdad de los conectores **conjunción** y **disyunción**
| p |  q  | p ∧ q | p v q |
|---|-----|-------|-------|
| T |  T  |   T   |   T   |
| T |  F  |   F   |   T   |
| F |  T  |   F   |   T   |
| F |  F  |   F   |   F   |

## Casos especiales
| p | p ∧ ¬p | p v ¬p |
|---|--------|--------|
| T |   F    |   T    |
| F |   F    |   T    |

## Leyes fundamentales

Así como en el álgebra elemental hay algunas leyes muy importantes y conocidas (conmutatividad, asociatividad, distribución, precedencia de operadores, etc.), en el álgebra Booleana también hay algunas leyes importantes que se deben tener en cuenta y pueden servir para replantear expresiones de formas que sean más sencillas.

* **Conmutatividad**: Tanto la conjunción como la disyunción son conmutativas, así que A ∨ B es equivalente a B ∨ A. También es cierto que A ∧ B es equivalente a B ∧ A.
* **Asociatividad**: Tanto la conjunción como la disyunción son asociativas, así que A ∨ (B ∨ C) es equivalente a (A ∨ B) ∨ C. Además, A ∧ (B ∧ C) es equivalente a (A ∧ B) ∧ C.
* **Distribución**: en el álgebra Booleana, la conjunción distribuye sobre la disyunción y viceversa. Esto quiere decir que:
    * A ∧ (B ∨ C) ≡ (A ∧ B) ∨ (A ∧ C)
    * A ∨ (B ∧ C) ≡ (A ∨ B) ∧ (A ∨ C)
* **Identidad de la conjunción**: si se hace una conjunción con el valor verdadero, el resultado es el mismo. Es decir que A ∧ Verdadero ≡ A.
* **Identidad de la disyunción**: si se hace una disyunción con el valor falso, el resultado es el mismo. Es decir que A ∨ Falso ≡ A.
* **Dominación de la conjunción**: si se hace una conjunción con el valor falso, el resultado es falso. Es decir que A ∧ Falso ≡ Falso.
* **Dominación de la disyunción**: si se hace una disyunción con el valor verdadero, el resultado es verdadero. Es decir que A ∨ Verdadero ≡ Verdadero.
* **Negación y equivalencia a falso**: es lo mismo decir que una proposición tiene un valor falso que decir que su negación tiene un valor positivo. Es decir que A ≡ Falso es lo mismo que decir ¬A ≡ Verdadero. Más aún, B ≡ Verdadero es lo mismo que decir B, así que A ≡ Falso se puede reescribir como ¬A.

## Leyes de De Morgan
* ¬(p ∧ q) ≡ ¬p ∨ ¬q
* ¬(p ∨ q) ≡ ¬p ∧ ¬q

## Simplificando expresiones lógicas
```Python
q ∧ q:             _____
q ∧ ¬q:            _____ 
q ∧ True:          _____ 
q ∧ False:         _____ 
q ∨ True:          _____ 
q ∨ False:         _____ 
¬q ∧ ¬q:           _____ 
¬q ∨ ¬q:           _____ 
¬(q ∨ p):          _____ 
¬(q ∧ p):          _____ 
(p ∧ q) ∨ (p ∧ r): _____ 
(p ∧ q) v (p ∧ r) v (q ∧ p): _____ 
```