'''Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. (Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.'''

def change_max(a: int, b: int):
    '''
    Esta funcion toma como parametros dos números y devuelve el mayor de ellos.

    Args:
        a: El primer número del parámetro.
        b: El segundo número del parámatro

    Returns:
        int: El mayor de Ambos
    '''

    if a > b:
        return a
    elif a < b:
        return b
    else:
        raise Exception('Hay un problema, los dos numero son iguales')
try:
    print(change_max(5, 8))
except Exception as e:
    print(e)