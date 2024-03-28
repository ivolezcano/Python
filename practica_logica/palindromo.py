'''Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.'''

def es_palindromo(param: str):
    '''Esta funcion toma como parametro un string y devuelve si es palíndromo o no (True or False)

    args:
        param(str): Toma un string como parametro 
    
    Returns: 
        bool: Devuelve si realmente es palíndromo o no.
    '''
    
    param = param.lower() # Convertir a minúsculas para comparar de forma genérica
    reverse = ''
    for i in param:
        reverse = i + reverse
    
    param = param.replace(' ','') # Reemplaza los espacios para verificar palindromos de mas de una palabra
    reverse = param.replace(' ','')

    if reverse == param:
        return True
    else:
        return False
    
    
    
print(es_palindromo('anita lava la tina'))
    