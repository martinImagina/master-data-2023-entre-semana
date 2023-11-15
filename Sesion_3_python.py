# Condicionales

# IF - ELIF (elif es opcional) - ELSE (else es opcional)

edad = 18

if (edad < 18):
  print('Menor de edad')
elif (edad >= 18 and edad < 40):
  print('Adulto Joven')
elif (edad >= 18 and edad < 70):
  print('Adulto')
else:
  print('Persona Mayor')

# BUCLES

lista_compra = [
    {
        "producto": "Leche",
        "precio": 2.00,
        "unidades": 6,
        "descuento": 0
    },
    {
        "producto": "Patatas",
        "precio": 5.00,
        "unidades": 10,
        "descuento": 0
    },
    {
        "producto": "Lechuga",
        "precio": 10.00,
        "unidades": 1,
        "descuento": 75
    },
]

# Bucle FOR para ITERAR por la lista y
# hacer un sumatorio de los precios de cada elemento y sacar el total de la cesta
# de la compra

print('''
******************** Ticket de Compra ************************''')
print(f"{'PRODUCTO':<10}| {'PRECIO':<10}| {'UNIDADES':<10}| {'DESCUENTO':<10}| {'TOTAL':<10}")
precio_total = 0
for elemento in lista_compra:
  precio_total_elemento = 0
  descuento_aplicado = 0
  producto = elemento["producto"]
  precio_elemento = elemento["precio"]
  unidades = elemento["unidades"]
  porcentaje_desc = elemento["descuento"]
  if (porcentaje_desc != 0):
    # Aplicamos el descuento
    precio_despues_del_descuento = precio_elemento * (1-(porcentaje_desc / 100))
    precio_total_elemento = precio_despues_del_descuento * unidades
    descuento_aplicado = unidades * precio_elemento * porcentaje_desc / 100
    #print('descuento_aplicado', descuento_aplicado)
  else:
    precio_total_elemento = precio_elemento * unidades
  
  precio_total += precio_total_elemento
  
  if(descuento_aplicado != 0):
    print(
        f'{producto:<15}{precio_elemento:<12}{unidades:<10} {descuento_aplicado:<10} {precio_total_elemento:<10}'
    )
  else:
    print(
        f'{producto:<15}{precio_elemento:<12}{unidades:<10} {"-":<10} {precio_total_elemento:<10}'
    )

# Salimos del bucle y ya tenemos el precio_total actualizado
print(f'''
--------------------------------------------------------------
Total:                                           {precio_total}€
''')




# BUCLES WHILE

lista = [1,2,3,4,5,6,7,8]

# Bucle WHILE para encontrar eliminar elementos hasta que la longitud sea 3
while (len(lista) > 3):
  lista.pop()
  print(lista)

# ¡OJO! Ejemplo de Bucle Infinito
''' 
while (True):
  print('Hola')
'''

opcion_escogida = ''

while(opcion_escogida != 'X'):
  opcion_escogida = input(
'''
Hola, escoge una opción:
1. Introducir Producto
2. Obtener Ticket Final
X. Salir del programa
''')
  if(opcion_escogida == '1'):
    nombre_producto = input('Indica el nombre del producto: ')
    print(f'Has ecogido: {nombre_producto}')
