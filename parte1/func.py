import math

def es_primo(num):
   
    if isinstance(num, bool):
        raise TypeError("La entrada no puede ser un valor booleano.")

    if not isinstance(num, (int, float)):
        raise TypeError("La entrada debe ser un número entero o flotante.")

    if isinstance(num, float) and not num.is_integer():
        if not math.isclose(num, round(num), abs_tol=1e-9):
            raise TypeError("La entrada debe ser un número entero o flotante cercano a un entero.")
        num = round(num)

    num = int(num)

    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True






