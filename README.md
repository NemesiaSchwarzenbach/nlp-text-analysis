#Análisis de Texto y NLP Básico

Este proyecto realiza un análisis básico de texto usando Python. Permite:

- Limpiar texto (minúsculas y eliminación de signos de puntuación)
- Listar palabras
- Quitar StopWords (palabras comunes que no aportan significado)
- Contar frecuencia de cada palabra
- Obtener el top n palabras más frecuentes
- Calcular palabras únicas y riqueza léxica

---

## Código principal

```python
from collections import Counter

# Funciones
def limpiar_texto(texto):
    resultado = texto.lower()
    signos = "¿?¡!:,."
    for s in signos:
        resultado = resultado.replace(s, "")
    return resultado

def lista_palabras(texto):
    return texto.split()

def quitar_stopw(lista):
    stopwords = {"el", "los", "la","las", "de", "que", "y", "en", "es", "a"}
    return [p for p in lista if p not in stopwords]

def ocurrencias(lista):
    return Counter(lista)

def top_n(counter, n):
    return counter.most_common(n)

def mas_frecuente(counter):
    if counter:
        return counter.most_common(1)[0]
    return None

def vocabulario_unico(lista):
    return len(set(lista))

def riqueza_lexica(lista):
    vocabulario = vocabulario_unico(lista)
    voc_total = len(lista)
    return round((vocabulario / voc_total),2)



#Ejemplo de uso
texto = """El lenguaje natural es fascinante. Las personas usamos el lenguaje para comunicarnos, pensar y crear ideas.
A veces el lenguaje es ambiguo, y otras veces es muy preciso.
Por eso estudiar el lenguaje natural con computadoras es un desafío interesante."""

limpio = limpiar_texto(texto)
lista_texto = lista_palabras(limpio)
sin_sw = quitar_stopw(lista_texto)
frecuencia = ocurrencias(sin_sw)

palabra_frecuente = mas_frecuente(frecuencia)
top10 = top_n(frecuencia, 10)
top5 = top_n(frecuencia, 5)

print(f'Top 10 palabras más frecuentes: {top10}')
print(f'Palabra más frecuente: {palabra_frecuente}')
print(f'Palabras únicas: {vocabulario_unico(sin_sw)}')
print(f'Riqueza léxica: {riqueza_lexica(sin_sw)}')

#Ejemplo de resultado
Top 10 palabras más frecuentes: [('lenguaje', 4), ('natural', 2), ('fascinante', 1), ('personas', 1), ...]
Palabra más frecuente: ('lenguaje', 4)
Palabras únicas: 18
Riqueza léxica: 0.78


#Tecnologías utilizadas
Python 3
Collections.Counter

Autor
Ayelén Apicella
https://www.linkedin.com/in/ayelen-apicella-03523521b



