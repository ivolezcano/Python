import re 
from colorama import Fore
import requests

website = 'https://www.vulnhub.com/'
resultado = requests.get(website)
content = resultado.text
# print(content)

patron = r'/entry/[\w-]*'
maquinas_repetidas = re.findall(patron, str(content))
# print(maquinas_repetidas)
sin_duplicados = list(set(maquinas_repetidas))
# print(sin_duplicados)

maquinas_final = []

for i in sin_duplicados:
    nombre_maquinas = i.replace('/entry/', '')
    maquinas_final.append(nombre_maquinas)
    print(nombre_maquinas)

