import requests


# Memory matters in transitional Peru



def linea():
    for i in range(40):
        print("=", end="")
    print()


def buscar_libro(titulo):
    url = "https://openlibrary.org/search.json"
    parametros = {
        "q": titulo,
        "fields": "key,title,author_name,first_publish_year",
    }
    respuesta = requests.get(url, params=parametros)
    if respuesta.status_code != 200:
        print("Error en la solicitud")
        return None
    return respuesta


def mostrar_doc(doc):
    titulo = doc.get("title", "Sin título")
    autores = ", ".join(doc.get("author_name", ["Desconocido"]))
    anio = doc.get("first_publish_year", "Desconocido")
    enlace = "https://openlibrary.org" + doc.get("key", "")
    linea()
    print("Título:", titulo)
    print("Autor(es):", autores)
    print("Año de publicación:", anio)
    print("Más información:", enlace)
    linea()


titulo_libro = ""
while titulo_libro == "":
    titulo_libro = input("Ingresa el título del libro: ").strip()

respuesta = buscar_libro(titulo_libro)

if respuesta is not None:
    datos = respuesta.json()
    docs = datos["docs"]

    print(respuesta.url)
    print("Documentos encontrados:", datos["numFound"])

    for doc in docs:
        mostrar_doc(doc)

    titulo_especial = ""
    while titulo_especial == "":
        titulo_especial = input("De la lista, escribe un título en especial: ").strip()

    encontrado = False
    for doc in docs:
        if titulo_especial.lower() in doc.get("title", "").lower():
            mostrar_doc(doc)
            encontrado = True

    if not encontrado:
        print("Ese título no está en la lista")
