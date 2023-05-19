import requests

# conexion por url de api, se pone la url como tal de la api a utilizar
#nombre de usuario estos son de prueba
#contraseña
#latitud y longitud en coordenadas decimales(formato simple)
#fecha a la cual quiere consultar
url_base = 'https://api.meteomatics.com'
username = "universidadcentral_alfonso"
password = "o5dP4GULo8"
location = '4.60971,-74.08175'
date = '2023-05-19'

#se arma la url con los parametros de la API que son fecha y hora, se ajusta la hora a la cual consultar la variable a tomar y el tipo de formato añadiendo la locacion, la fecha y la url_base
#con la funcion get se trae la respuesta de la API o de la pagina web
url = f'{url_base}/{date}T00:00:00Z/t_2m:C,relative_humidity_2m:p/{location}/json' 
response = requests.get(url, auth=(username, password))

#se mira el estatus de respuesta de la API 200 es exitoso 401 es incorrecto
if response.status_code !=200:
    print("la temperatura no se encontro, conexion fallida")
else:
    print("conexion exitosa")

#si la conexion es exitosa se realiza la consulta y el ajuste de los datos segun el formato que devuelva la API(formato JSON)
#la temperatura tiene un error de dos grados. pero sirve para una estimatizacion tambien la humedad.
#se ajustan los valores con un porcentaje de error del 5%
if response.status_code == 200:
    data = response.json()
    temperatura = data['data'][0]['coordinates'][0]['dates'][0]['value']
    humedad = data['data'][1]['coordinates'][0]['dates'][0]['value']
    print(f'la temperatura de la ubicacion {location}, en el dia {date}: {temperatura}°C')
    print(f'la humedad relativa de la ubicacion {location}, en el dia {date}: {humedad}%')
    
else:
    print("no se encontro la temperatura y humedad deseada")


