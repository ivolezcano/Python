'''Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto que python tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio.'''

cadena = (1, 2, 3, 'Verde', 'mesa')

def new_len(args: str):
    '''
    Funcion que toma como parametro un string o un lista y te devuelve su longitud.

    Args:
        args (str/list): El parametro puede ser una cadena de texto o una  lista.
    
    Returns:
        int: La funcion retorna la longitud del parametro recibido.
    '''

    contador = 0
    for i in args:
        contador+=1
    return contador

print(f'la longitud de la cadena es: {new_len(cadena)}')