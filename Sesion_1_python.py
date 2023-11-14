# Imprimir Hola Mundo en python
print("Hola Mundo")

# Declaración y Asignación de valor de una variable
nombre = "Martín"

# Concatenar Textos
print("Hola" + " " + nombre)

# Formateo de Textos
print(f"Hola {nombre}")

# Tipar variable - Tipo Texto (STR)
apellidos: str = "San José de Vicente"

# Concatenar texto y asignar a una variable nueva
nombre_completo = f"{nombre} {apellidos}"

print("Hola " + nombre_completo)

# Declarar variable de tipo numérico entero (INT)
edad: int = 32
print(f"{nombre_completo} tiene {edad} años")


# Declarar variable numérica DECIMAL de COMA FLOTANTE
altura: float = 1.70

# Operación de Suma
print(f"{nombre} ha cumplido años y ahora tiene {edad + 1} años")

print(f"La edad nueva es {edad}")

# Operación de Incremento Numérico
edad = edad + 1

# Operación de Autoincremento
edad += 1

# Operación de Multiplicar la Edad x 2
edad = edad * 2

# Operación de AutoMultiplicación
edad *= 2

# Operación de Elevado a 2
edad = edad**2

# Operación de AutoPotencia
edad **= 2


# Operación de División
altura = altura / 2

# Operación para obtener el RESTO de una División
resto = edad%2

# Declaración y Asignación de CONSTANTES
NUMERO_PI = 3.1416


# Asignación y declaración de valores BOOLEANOS: Verdadero / Falso
tiene_hijos = True
casado = False


# Lista de la compra con [] 
lista_de_la_compra = ["Patatas", "Leche", 'Filetes']

# Mostrar por consola una lista
print(lista_de_la_compra)

# Mostrar todos los elementos de una lista por consola
print(*lista_de_la_compra)

# Obtener el primer elemento de la lista
print(lista_de_la_compra[0])

# Obtener el último elemento de la lista
print(lista_de_la_compra[2])

# ERROR: Obtener un elemento que no existe
# print(lista_de_la_compra[3])

# Añadir elemento a una lista
lista_de_la_compra.append("Manzanas")
print(lista_de_la_compra)

# Obtener rangos de elementos de una lista
print(lista_de_la_compra[0:2])

# Solo Patatas
print(lista_de_la_compra[0:1])

# Mostrar Todos los datos
print(lista_de_la_compra[0:])

# Mostrar Todos los elementos de 2 en 2
print(lista_de_la_compra[0::2])

# Mostrar Todos los elementos de una lista al revés
print(lista_de_la_compra[::-1])

# Opción que cambia el orden de la lista original
# lista_de_la_compra.reverse()
# print(lista_de_la_compra)

# Realizar una copia de una lista como mejor opción
copia_lista_compra = lista_de_la_compra.copy()

# Creación d eotra variable apuntando al mismo valor
# OJO: Paso por Referencia. Una modifica a la otra y viceversa
copia_2_lista_compra = lista_de_la_compra

lista_de_la_compra.append('Cereales')
print(copia_lista_compra)
print(copia_2_lista_compra)


# Eliminar el último valor de una lista
lista_de_la_compra.pop()
print(lista_de_la_compra)

# Eliminar un elemento de la lista por índice
lista_de_la_compra.pop(0)
print(lista_de_la_compra)

# Eliminar un elemento por valor
lista_de_la_compra.remove('Filetes')
print(lista_de_la_compra)

lista_de_la_compra.append('Filetes')
lista_de_la_compra.append('Filetes')
lista_de_la_compra.append('Filetes')
print(lista_de_la_compra)

# Demostración de que solo elimina la primera coincidencia
lista_de_la_compra.remove('Filetes')
print(lista_de_la_compra)

# Limpiar la lista de la compra - Quitar todos los elementos
lista_de_la_compra.clear()
print(lista_de_la_compra)


lista_de_la_compra=['Agua', 'Cocacola', 'Cerveza']

# Insertar elementos en una lista por posición
lista_de_la_compra.insert(2, 'Sprite')
print(lista_de_la_compra)

# Actualizar un elemento de la lista
lista_de_la_compra[2] = 'Fanta'
print(lista_de_la_compra)
