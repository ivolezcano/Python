'''Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.'''



def is_vocal(caract: str):
    '''
        Esta funcion recibe como parámetro 1 Caracter y devuelve True si es vocal de lo contrario devuelve False.

    Args:
        caract (str): Caracter a verificar si es vocal.
        
    Returns:
        bool (True/False): Si el caracter es vocal 
    '''
    vocal = 'aeiouAEIOU'

    if len(caract) > 1: # Chequear que se pase un solo caracter
        raise Exception('ERROR ! Ingresaste más de un caracter')

    if caract in vocal:
        return True
    else:
        return False

try:
    print(is_vocal('a'))
except Exception as e:
    print(e)