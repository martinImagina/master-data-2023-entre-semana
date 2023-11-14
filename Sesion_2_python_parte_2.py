alumno1 = {
  "nombre":"Martín",
  "email": "martin@imaginagroup.com",
  "cursos": [
    {
      "nombre":"Python",
      "examenes": [
        {
          "nombre": "Sesión 1",
          "duracion": 2.5,
          "nota": 9
        },
        {
          "nombre": "Sesión 2",
          "duracion": 1.5,
          "nota": 7
        }
      ]
    }
  ]
}

alumno2 = {
  "nombre":"David",
  "email": "david@imaginagroup.com",
  "cursos": [
    {
      "nombre":"Python",
      "examenes": [
        {
          "nombre": "Sesión 1",
          "duracion": 2.5,
          "nota": 5
        },
        {
          "nombre": "Sesión 2",
          "duracion": 1.5,
          "nota": 4
        }
      ]
    },
    {
      "nombre":"Java",
      "examenes": [
        {
          "nombre": "Sesión 1: Fundamentos",
          "duracion": 3.5,
          "nota": 6
        },
        {
          "nombre": "Sesión 2: Métodos",
          "duracion": 3.5,
          "nota": 8
        }
      ]
    }
  ]
}


lista_master = []

lista_master.append(alumno1) # lista_master[0]
lista_master.append(alumno2) # lista_master[1]

# print(f'- Alumno 1: { lista_master[0] } ')


# Primer ejercicio: Obtener el nombre del alumno 1 desde la lista
nombre = lista_master[0]["nombre"]
print(f'El nombre del Alumno 1 es: { nombre }')

# Segundo ejercicio: Obtener la nota del segundo examen del segundo curso del alumno 2 
# en la lista_master
alumno = lista_master[1]
nota = lista_master[1]["cursos"][1]["examenes"][1]["nota"]

print(f'La nota de {alumno["nombre"]} es {nota}/10')





