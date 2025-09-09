import unicodedata

def normalizar_texto(texto: str) -> str:
    # Pasa el texto a minúsculas para evitar diferencias por mayúsculas/minúsculas
    texto = texto.lower()
    # Descompone los caracteres (ej: "á" -> "a" + acento)
    texto = unicodedata.normalize("NFD", texto)
    # Filtra los acentos y caracteres especiales, dejando solo los básicos
    texto = "".join(c for c in texto if unicodedata.category(c) != "Mn")
    return texto

# Ejemplo de uso
base = ["canciÓn", "niño", "árbol", "pingüino"]
busqueda = "pingUino"  # El usuario escribió sin tilde

# Normalizamos ambos lados para comparar

resultado = []
for palabra in base:
    if normalizar_texto(busqueda) in normalizar_texto(palabra):
        resultado.append(palabra)

print(resultado)  # ['árbol']
