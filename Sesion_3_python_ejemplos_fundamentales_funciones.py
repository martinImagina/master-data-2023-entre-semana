# No se puede llamar a funciones no declaradas antes
# El orden importa
# mostrar_saludo()

# Declaración de Funciones sin parámetros
def mostrar_saludo():
  print('Hola, Martin')

# Llamada y ejecución de funciones sin parámetros
mostrar_saludo()

# Funciones con parámetros (con tipos o sin tipos)
def mostrar_despedida(nombre: str, apellidos: str):
  nombre_completo = f'{nombre} {apellidos}'
  print(f'Hasta la vista, Sr. {nombre_completo}')


# Llamada y ejecución de funciones con parámetros
mostrar_despedida('Martín', 'San José') # El orden por defecto
mostrar_despedida(nombre='Martín', apellidos='San José') # Especificar el parámetro por clave
mostrar_despedida(apellidos='San José', nombre='Martín') # Especificar el parámetro por clave desordenada
# mostrar_despedida(nombre='Martín', 'San José') # ERROR: No se puede pasar por clave y luego orden
mostrar_despedida('Martín', apellidos='San José') # Especificar el parámetro por oden y clave


# Funciones con un parámeto por defecto
def saludar_mundo(publico: str = 'Mundo'):
  print(f'¡Hola, {publico}! ¿Qué tal estás?')

saludar_mundo() # Hola, Mundo
saludar_mundo('clase')


# Funciones con RETORNO
def saludar_sin_espacios(nombre: str, apellidos: str) -> str:
  # Eliminamos los caracteres en blanco del nombre y apellido (tanto delante como detrás)
  nombre_completo = f'{nombre.strip()} {apellidos.strip()}'
  return nombre_completo

nombre_sin_espacios = saludar_sin_espacios(' Martin ', 'San José ')

print(f'Hola, {nombre_sin_espacios}')
print(f"Hola, {saludar_sin_espacios(' Martin ', 'San José ')}")



# Función dentro de otra función
# Funciones con RETORNO
def imprimir_saludo_sin_espacios(nombre: str, apellidos: str):
  # Eliminamos los caracteres en blanco del nombre y apellido (tanto delante como detrás)
  nombre_completo = f'{nombre.strip()} {apellidos.strip()}'
  saludar_mundo(nombre_completo)


imprimir_saludo_sin_espacios(' Martin ', 'San José ')


