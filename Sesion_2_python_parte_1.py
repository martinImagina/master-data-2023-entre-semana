# Ejemplo Cadenas de texto con mútiples líneas

# Las cadenas de texto se limitan con comillas
# Puedens er comillas simples ' ... '
# Comillas dobles: " ... "
# O comillas triples (simples y dobles) """ ... """
# ''' ... '''
miCadena1:str = 'Hola, Mundo'
miCadena2:str = "Hola Mundo"

miCadena3:str = '''
Hola Mundo
    Hola Mundo
Hola Mundo
'''

miCadena4:str = """
Hola Mundo
    Hola Mundo
Hola Mundo"""

# print(miCadena4)



# Los diccionarios sirven para almacenar datos en formato de clave - valor
# Se delimitan a través de llaves { ... }

alumno = {
    "nombre": "Martin",
    "apellidos": "San José",
    "edad": 28,
    "email": "masajo@edem.es"
}

# print(f'El nombre del alumno es: { alumno["nombre"] }')

# Martín San Jose tiene 28 años
# print(f'{ alumno["nombre"] } { alumno["apellidos"] } tiene {alumno["edad"]} años.')

# Añadir nuevas claves que no existían es posible
alumno['altura'] = 1.7
# print(f'La altura del alumno es: {alumno["altura"] } metros')

# Tipo NONE --> La ausencia de valor
alumno['altura'] = None
print(f'La altura del alumno es: {alumno["altura"] } metros')


alumno1 = {
  "nombre": "Martín",
  "email": "martin@imaginagroup.com",
  "cursos": [
    {
      "curso": "Python",
      "examenes": [
        {
          "sesion_1": "Fundamentos de Python",
          "nota": 9
        },
        {
          "sesion_2": "Tipos complejos y estructuras en Python",
          "nota": 5
        }
      ]
    },
    {
      "curso": "Javascript",
      "examenes": [
        {
          "sesion_1": "Fundamentos de Javascript",
          "nota": 0
        },
        {
          "sesion_2": "Tipos complejos y estructuras en Javascript",
          "nota": 2
        }
      ]
    },
  ]
}







puntos = None
# puntos += 1 --> No se puede operar con valores vacios (NONE)
puntos = 2 # Tendríamos que darle un alor para hacer algo con él
puntos += 1

# Accediendo al tamaño de una lista
lista_alumnos = ["Martín", "Silvia", "Alberto"]
# print(f'El número de elementos de la lista es: { len(lista_alumnos) }')
# print(f'El número de elementos de la lista es: { lista_alumnos.__len__() }')

# Imprimir los valores de una lista
# print(f'La lista es: { lista_alumnos }')
# print(*lista_alumnos)
# print(f'La lista es: { lista_alumnos.__str__() }')
# print(f'La lista es: { str(lista_alumnos) }')

'''
print(f'La lista es: { lista_alumnos.__repr__() }')
print(f'La lista es: { repr(lista_alumnos) }')
'''




### MUY IMPORTANTE

# Ejemplos de asigación por REFERENCIA --> ¡muy importante!

# 1. listas

lista = ["Leche", "Agua", "Zumo"]
lista2 = lista

lista2.append('Limones')
# print(*lista)


# 2. Diccionarios
alumno = {
    "nombre": "Martin",
    "apellidos": "San José",
    "edad": 28,
    "email": "masajo@edem.es"
}
alumno2 = alumno

alumno2['nombre'] = 'Javier'
# print(f'{ alumno["nombre"] } { alumno["apellidos"] } tiene {alumno["edad"]} años.')

# Ejemplos de Asignación por Valor

# 1. Booleanos
tiene_coche = True
tiene_moto = tiene_coche

tiene_moto = False
# print(f'¿Tiene coche? {tiene_coche}')


# 2. Números
edad = 10
edad2 = edad

edad2 = 11
# print(f'La edad es: {edad}')

# 3. Cadénas de texto
coche = 'Audi'
coche2 = coche

coche2= 'Fiat'
# print(f'El coche es un {coche}')










