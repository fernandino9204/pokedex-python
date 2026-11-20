# Proyecto final: Pokédex con Python

Aplicación de consola que consulta la [PokéAPI](https://pokeapi.co/) mediante HTTP GET, muestra estadísticas y guarda cada consulta exitosa en JSON.

## Requisitos
- Python 3.10 o superior
- Internet
- Biblioteca `requests`

## Instalación
```bat
py -m pip install -r requirements.txt
```

## Ejecución
```bat
py pokedex_final.py
```
Selecciona `1`, escribe `pikachu` y presiona Enter. El programa muestra nombre, peso (hectogramos), altura (decímetros), tipos, habilidades, movimientos y la URL de la imagen frontal. Cada búsqueda exitosa crea un JSON nuevo en `pokedex/`. Selecciona `2` para salir.

## Manejo de errores
- HTTP 200: Pokémon encontrado.
- HTTP 404: Pokémon no encontrado.
- Otros estados HTTP: se informa el código.
- Timeout: la solicitud tiene un límite de 10 segundos.
- Fallos de red: se captura `RequestException`.

## Archivos
- `pokedex_final.py`: programa principal comentado.
- `requirements.txt`: dependencias.
- `pokedex/`: archivos JSON generados durante las consultas.
- `evidencias/`: capturas reales de la ejecución para agregar antes de entregar.

## Ejemplo de búsqueda exitosa
```text
===== MENÚ POKÉDEX =====
1. Buscar Pokémon
2. Salir
Selecciona una opción: 1
Ingresa el nombre del Pokémon: pikachu
Pokémon encontrado.
Nombre: pikachu
Peso: 60 hectogramos
Altura: 4 decímetros
```

## Evidencias reales de ejecución

Las siguientes capturas deben tomarse al ejecutar el proyecto en una computadora. Guarda las imágenes PNG dentro de `evidencias/` usando **exactamente** estos nombres. Las referencias ya están configuradas para mostrarlas automáticamente en GitHub.

### Evidencia 1. Búsqueda exitosa de Pikachu

Ejecuta `py pokedex_final.py`, selecciona `1`, busca `pikachu` y captura la consola con el nombre, peso, altura, tipos y habilidades.

![Búsqueda exitosa de Pikachu](evidencias/busqueda_exitosa.png)

### Evidencia 2. Movimientos e imagen frontal

En la misma ejecución, captura la consola donde se muestran los movimientos y la URL de la imagen frontal (`sprites`).

![Movimientos y URL de imagen frontal](evidencias/movimientos_pokemon.png)

### Evidencia 3. JSON generado

Abre el archivo `.json` creado en `pokedex/` con Bloc de notas o VS Code y captura el contenido real.

![Archivo JSON generado](evidencias/archivo_json.png)

**Nota:** Las imágenes anteriores solo se visualizarán cuando agregues tus capturas reales. No se incluyen capturas ficticias.

## Librerías utilizadas

- `requests`: realiza solicitudes HTTP a PokéAPI. Es la única dependencia externa y se instala desde `requirements.txt`.
- `os`: crea carpetas y construye rutas de archivos (incluida en Python).
- `json`: lee y escribe datos JSON (incluida en Python).
- `datetime`: genera marcas de tiempo para cada archivo (incluida en Python).

## Publicar en GitHub
1. Entra a https://github.com/new e inicia sesión.
2. Crea un repositorio público llamado `pokedex-python`.
3. Abre el repositorio, selecciona **Add file > Upload files** y sube los archivos y carpetas del proyecto (con las capturas reales y al menos un JSON generado).
4. Selecciona **Commit changes**.
5. Comprueba que las imágenes aparecen en el README de la página principal.

Sube `pokedex_final.py`, `requirements.txt`, `README.md`, la carpeta `pokedex/` con JSON generados y `evidencias/` con tus capturas. No incluyas credenciales ni datos personales.

## Fuente de datos
[PokéAPI](https://pokeapi.co/)
