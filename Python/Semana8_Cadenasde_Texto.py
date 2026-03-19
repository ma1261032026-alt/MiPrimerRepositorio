# las comillas triples son las que se encargan de hacer
# Cadenas de texto largas sin mdoficar el formato.
# texto corto
poema = "  "

# textos largos ''' o """
poema = """Es porque un pajarito de la montaña ha hecho,
en el hueco de un árbol, su nido matinal,
que el árbol amanece con música en el pecho,
como que si tuviera corazón musical.

Si el dulce pajarito por entre el hueco asoma,
para beber rocío, para beber aroma,
el árbol de la sierra me da la sensación
de que se le ha salido, cantando, el corazón. """

Cancion = """Se te olvida, que me quieres a pesar de lo que dices
Pues llevamos, en el alma, cicatrices imposibles de borrar
Se te olvida que hasta puedo hacerte mal si me decido
Pues tu amor lo tengo muy comprometido
Pero a fuerza no será"""

## print(poema)

## computadora -> que variable queres imprimir
## print() ->
# void -> no devuelve nada
# objeto -> devuelve un tipo de dato

## realizar una wiki tambien pueden darle doble clic al documento y se les
## despliega el editor de texto

## Mayusculas
## multabilidad -> siempre debemos evitar transformar objeto original
## clases -> estereotipo (como un molde)
## propiedades ->
## color
## tipo de motor (electricidad o de gas)
## Ojos
## color de pelo

## funciones -> string (cadenas de texto) es un objeto
## moverse
## frenar
## cargarse
## descargarse

# Song es un espacio de memoria para string
# se va a llenar con le contenido de Cancion alterar con la accion upper (mayusculas)

Cancion_Mayusculas = Cancion.upper()
print(Cancion_Mayusculas)

Cancion_minuscula = poema.lower()
print(Cancion_minuscula)

## tiene que ingresar 100 nombres en mayuscula
mensaje = "hOlA kACe progRMando o qUe HaCe"
## Capitalize a que la primera letra de cada palabra sea mayuscula
mensajeCorrecto = mensaje.capitalize()
# print(mensajeCorrecto)

## Las flipantess aventuras de el gato con bolson magico y alfredo
titulo = "Las flipantess aventuras de el gato con bolson magico y alfredo"
tituloCorrecto = titulo.title()
# print(tituloCorrecto)

## swapCase() permite cambiar entre mayusculas y minusculas
swapCaseTitulo = tituloCorrecto.swapcase()
print(swapCaseTitulo)

## metodos de validacion
numero = "512"
solo_letras = "El chico del apartamentos "
Coro = "piribiribanban"

quieroSoloLetras = numero.isalpha()
print(quieroSoloLetras)

## numeros y letras
print("numeros y letras")
numeros_letras = nombre + numero
evaluarTexto = numeros_letras.isalnum()
print(evaluarTexto)

## verificar que solo sean numeros
print("verificar que solo sean numeros")
solo_numeros = numero.isdigit()
print(solo_numeros)
