'''Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.'''

def sum(numbers: int):
    '''Toma como parametro una lista de números y devuelve la suma de todos.
    
    Args:
        numbers (list[int]): La lista de números

    Return:
        int: Devuelve  la suma total de los numeros
    '''
    total = 0

    for i in numbers:
        total = total + i

    return total 

def multip(numbers):
    total = 1

    for i in numbers:
        total = total * i

    return total

numeros = (1, 2, 3, 4)
# Prueba de suma
print(sum(numeros))
# Prueba de multiplicación
print(multip(numeros))