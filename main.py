import requests

# Definimos las credenciales de autenticación
username = 'HX-FNegrete'
token = input('Ingresa tu Token Personal de Seguridad: ')

# Defimos la URL del repo 
url = 'https://raw.githubusercontent.com/soyHenry/DS-M2-Checkpoint/blob/main/Generador-CP/CP_07_2.md'

# Enviamos la solicitud HTTP autenticada
response = requests.get(url, auth=(username, token))

# Si la solicitud fue exitosa, se lee el contenido del archivo Markdown
if response.ok:
    markdown_content = response.text
    print(markdown_content)
else:
    print('No se pudo leer el archivo')

