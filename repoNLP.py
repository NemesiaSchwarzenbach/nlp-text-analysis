"""
Proyecto: Análisis de texto en español

Este proyecto realiza un análisis básico de texto:
- Limpieza de signos de puntuación
- Tokenización en palabras
- Eliminación de StopWords
- Conteo de ocurrencias de palabras
- Identificación de palabras más frecuentes
- Cálculo de vocabulario único y riqueza léxica

Herramientas: Python estándar + collections.Counter
Autor: Ayelén Apicella
"""

from collections import Counter

# ----------------------------
# Funciones
# ----------------------------

def limpiar_texto(texto):
    """Convierte a minúsculas y elimina signos de puntuación."""
    resultado = texto.lower()
    signos = "¿?¡!:,."
    for s in signos:
        resultado = resultado.replace(s, "")
    return resultado
    
def lista_palabras(texto):
    """Divide el texto en palabras (tokens)."""
    return texto.split()

def quitar_stopw(lista):
    """Elimina StopWords comunes en español."""
    stopwords = {"el", "los", "la","las", "de", "que", "y", "en", "es", "a"}
    return [p for p in lista if p not in stopwords]

def ocurrencias(lista):
    """Cuenta cuántas veces aparece cada palabra."""
    return Counter(lista)

def top_n(counter, n):
    """Devuelve las n palabras más frecuentes."""
    return counter.most_common(n)

def mas_frecuente(counter):
    """Devuelve la palabra más frecuente."""
    if counter:
        return counter.most_common(1)[0]
    return None
    
def vocabulario_unico(lista):
    """Cuenta la cantidad de palabras distintas."""
    return len(set(lista))

def riqueza_lexica(lista):
    """Calcula la riqueza léxica: vocabulario único / total de palabras."""
    vocabulario = vocabulario_unico(lista)
    voc_total = len(lista)
    return round((vocabulario / voc_total), 2)


# ----------------------------
# Ejemplo de uso
# ----------------------------

texto = """El lenguaje natural es fascinante. Las personas usamos el lenguaje para comunicarnos, pensar y crear ideas.
A veces el lenguaje es ambiguo, y otras veces es muy preciso.
Por eso estudiar el lenguaje natural con computadoras es un desafío interesante."""

# 1. Limpieza y tokenización
limpio = limpiar_texto(texto)
lista_texto = lista_palabras(limpio)
sin_sw = quitar_stopw(lista_texto)

# 2. Conteo de palabras
frecuencia = ocurrencias(sin_sw)
palabra_frecuente = mas_frecuente(frecuencia)
top10 = top_n(frecuencia, 10)
top5 = top_n(frecuencia, 5)

# 3. Métricas de vocabulario
q_no_repetidas = vocabulario_unico(sin_sw)
riquezaLexica = riqueza_lexica(sin_sw)

# 4. Resultados
print("=== Análisis de Texto ===")
print(f"Total palabras: {len(lista_texto)}")
print(f"Palabras sin StopWords: {len(sin_sw)}")
print(f"Vocabulario único: {q_no_repetidas}")
print(f"Riqueza léxica: {riquezaLexica}")
print(f"Palabra más frecuente: {palabra_frecuente[0]} ({palabra_frecuente[1]} veces)\n")

print("*** Top 10 palabras ***")
for palabra, freq in top10:
    print(f"{palabra}: {freq}")

print("\n*** Top 5 palabras ***")
for palabra, freq in top5:
    print(f"{palabra}: {freq}")