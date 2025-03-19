# Resolución del Challenge de testing con AI

## Función es primo

Primero le pedí a Gemini que me explicara el funcionamiento de la función inicial
![Texto alternativo](imagenes/explicacion-funcion.png)

Luego le dí una lista de especificaciones que debía cumplir la función
![Texto alternativo](imagenes/especificaciones.png)

Su primer intento fue:
![Texto alternativo](imagenes/primer-intento.png)

Al ver que no cumplía con una de las especificaciones (No lanzaba el TypeError cuando el dato recibido era un booleano) le pedí que me diera una solución, y me dio la siguiente función:
![Texto alternativo](imagenes/segunto-intento.png)

## Realización de test

Directamente desde el archivo con el chatbot de Qodo realicé los test, modificando ciertas partes del código para que cumplieran con las especificaciones. Y agregando algunas pruebas más.
![Texto alternativo](imagenes/tests.png)

## Tests

Al correr los tests, todos pasaron correctamente.

Tanto los tests de reference_test.py
![Texto alternativo](imagenes/test-reference.png)

Como los tests de func_test.py
![Texto alternativo](imagenes/test-func.png)

## Coverage

![Texto alternativo](imagenes/coverage.png)
