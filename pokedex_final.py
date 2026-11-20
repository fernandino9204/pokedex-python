import os
import json
import requests
from datetime import datetime

API_URL = 'https://pokeapi.co/api/v2/pokemon/'
CARPETA = 'pokedex'


def crear_carpeta():
    """Crea el directorio local para las consultas."""
    os.makedirs(CARPETA, exist_ok=True)


def consultar_pokemon(nombre):
    """Consulta la API y gestiona estados HTTP y errores de red."""
    try:
        respuesta = requests.get(API_URL + nombre.lower().strip(), timeout=10)
        if respuesta.status_code == 200:
            print('\nPokémon encontrado.')
            return respuesta.json()
        if respuesta.status_code == 404:
            print('\nPokémon no encontrado.')
        print('Error HTTP:', respuesta.status_code) if respuesta.status_code != 404 else None
    except requests.exceptions.Timeout:
        print('Error: tiempo de espera agotado.')
    except requests.exceptions.RequestException as error:
        print('Error de conexión:', error)
    return None


def extraer_datos(pokemon):
    """Selecciona las estadísticas, listas e imagen frontal."""
    return {
        'nombre': pokemon['name'],
        'peso': pokemon['weight'],
        'altura': pokemon['height'],
        'tipos': [x['type']['name'] for x in pokemon['types']],
        'habilidades': [x['ability']['name'] for x in pokemon['abilities']],
        'movimientos': [x['move']['name'] for x in pokemon['moves']],
        'imagen_frontal': pokemon['sprites']['front_default'],
    }


def mostrar_datos(datos):
    """Presenta la información obtenida en la consola."""
    print('\n========== POKÉDEX ==========')
    print('Nombre:', datos['nombre'])
    print('Peso:', datos['peso'], 'hectogramos')
    print('Altura:', datos['altura'], 'decímetros')
    print('Tipos:', ', '.join(datos['tipos']))
    print('Habilidades:', ', '.join(datos['habilidades']))
    print('\nMovimientos:')
    for movimiento in datos['movimientos']:
        print('-', movimiento)
    print('\nImagen frontal:', datos['imagen_frontal'])
    print('=============================')


def guardar_json(datos):
    """Guarda una consulta exitosa en un JSON nuevo."""
    crear_carpeta()
    fecha = datetime.now().strftime('%Y%m%d_%H%M%S_%f')
    ruta = os.path.join(CARPETA, f"{datos['nombre']}_{fecha}.json")
    with open(ruta, 'w', encoding='utf-8') as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)
    print('\nArchivo JSON guardado en:', ruta)


def main():
    """Permite consultar varios Pokémon desde un menú."""
    crear_carpeta()
    while True:
        print('\n===== MENÚ POKÉDEX =====')
        print('1. Buscar Pokémon')
        print('2. Salir')
        opcion = input('Selecciona una opción: ').strip()
        if opcion == '1':
            nombre = input('Ingresa el nombre del Pokémon: ').strip()
            if not nombre:
                print('Debes ingresar un nombre.')
                continue
            pokemon = consultar_pokemon(nombre)
            if pokemon is not None:
                datos = extraer_datos(pokemon)
                mostrar_datos(datos)
                guardar_json(datos)
        elif opcion == '2':
            print('Gracias por utilizar la Pokédex.')
            break
        else:
            print('Opción no válida.')


if __name__ == '__main__':
    main()
