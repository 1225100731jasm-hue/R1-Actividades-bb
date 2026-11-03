import requests

URL_BASE = "https://www.thesportsdb.com/api/v1/json/123/"
ENCABEZADOS = {"User-Agent": "Mozilla/5.0"}


def linea():
    for i in range(40):
        print("=", end="")
    print()


def consultar(endpoint, parametros=None):
    respuesta = requests.get(URL_BASE + endpoint, params=parametros, headers=ENCABEZADOS)
    if respuesta.status_code != 200:
        print("Error en la solicitud")
        return None
    return respuesta.json()


def pedir_texto(mensaje):
    texto = input(mensaje).strip()
    while texto == "" or texto.isdigit():
        print("Entrada no válida, escribe texto (no números)")
        texto = input(mensaje).strip()
    return texto


def pedir_entero(mensaje):
    valor = input(mensaje).strip()
    while not valor.isdigit():
        print("Entrada no válida, escribe un número entero")
        valor = input(mensaje).strip()
    return int(valor)


def dato(diccionario, clave):
    valor = diccionario.get(clave)
    if valor is None or valor == "":
        return "No disponible"
    return valor


def consultar_equipo():
    nombre = pedir_texto("Nombre del equipo: ")
    data = consultar("searchteams.php", {"t": nombre})
    if data is None:
        return
    if data["teams"] is None:
        print("No se encontró el equipo")
        return
    equipo = data["teams"][0]
    linea()
    print("Equipo:", dato(equipo, "strTeam"))
    print("Liga:", dato(equipo, "strLeague"))
    print("Descripción en español:", dato(equipo, "strDescriptionES"))
    print("Página oficial:", dato(equipo, "strWebsite"))
    print("Estadio:", dato(equipo, "strStadium"))
    linea()


def consultar_jugador():
    nombre = pedir_texto("Nombre del jugador: ")
    data = consultar("searchplayers.php", {"p": nombre})
    if data is None:
        return
    if data["player"] is None:
        print("No se encontró el jugador")
        return
    jugador = data["player"][0]
    linea()
    print("Nombre completo:", dato(jugador, "strPlayer"))
    print("Nacionalidad:", dato(jugador, "strNationality"))
    print("Equipo:", dato(jugador, "strTeam"))
    print("Lugar de nacimiento:", dato(jugador, "strBirthLocation"))
    print("Facebook:", dato(jugador, "strFacebook"))
    print("Altura:", dato(jugador, "strHeight"))
    print("Peso:", dato(jugador, "strWeight"))
    linea()


def listar_ligas():
    data = consultar("all_leagues.php")
    if data is None:
        return
    if data["leagues"] is None:
        print("No se encontraron ligas")
        return
    linea()
    for liga in data["leagues"]:
        print("ID:", dato(liga, "idLeague"), "- Liga:", dato(liga, "strLeague"))
    linea()


def consultar_liga():
    id_liga = pedir_entero("ID de la liga (ejemplo 4346): ")
    data = consultar("lookupleague.php", {"id": id_liga})
    if data is None:
        return
    if data["leagues"] is None:
        print("No se encontró la liga")
        return
    liga = data["leagues"][0]
    linea()
    print("ID:", dato(liga, "idLeague"))
    print("Liga:", dato(liga, "strLeague"))
    print("Deporte:", dato(liga, "strSport"))
    print("País:", dato(liga, "strCountry"))
    print("Año de fundación:", dato(liga, "intFormedYear"))
    print("Página oficial:", dato(liga, "strWebsite"))
    print("Descripción:", dato(liga, "strDescriptionEN"))
    linea()


def menu():
    opcion = 0
    while opcion != 5:
        print("1. Consultar equipo")
        print("2. Consultar jugador")
        print("3. Listado de ligas")
        print("4. Consultar una liga")
        print("5. Salir")
        opcion = pedir_entero("Elige una opción: ")
        if opcion == 1:
            consultar_equipo()
        elif opcion == 2:
            consultar_jugador()
        elif opcion == 3:
            listar_ligas()
        elif opcion == 4:
            consultar_liga()
        elif opcion == 5:
            print("Hasta luego")
        else:
            print("Opción no válida")


menu()