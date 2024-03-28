'''Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"'''

def inversa(phrase: str):
    '''Devuelve el parametro invertido
    Arg:
        phrase(str): Un string que se desee invertir 

    Return:
        str: El string invertido
    '''
    reverse = ''
    for i in phrase:
        reverse = i + reverse
    
    return reverse

print(inversa('Estoy probando'))
