'''Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.'''

def max_de_tres(a: int, b: int, c: int):
    '''
        Esta funcion toma tres parametros (int) y devuelve el mayor de ellos. 
    
    Args:
        a: Primer Argumento
        b: Segundo Argumento
        c: Tercer Argumento

    Returns:
        int: El valor númerico mayor de los tres argumentos.
    '''
    if a == b and b == c:
        raise Exception('Los 3 valores son iguales. Ingrese nuevos') 

    arr = [a, b, c]
    max = 0
    for i in arr:
        if i > max:
            max = i
    return max

try:
    print(max_de_tres(8, 8, 8))
except Exception as e:
    print(e)

