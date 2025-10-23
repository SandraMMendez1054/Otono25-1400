# Programa para gestionar las notas de los estudiantes

# Función que muestra el menú principal

def mostrar_menu():
    print("\n" + "=" * 30)
    print("\tGESTOR DE NOTAS")
    print("=" * 30)
    print("1. Agregar estudiante")
    print("2. Mostrar todos")
    print("3. Salir")
    print("4. Eliminar estudiante por nombre")
    print("5. Buscar estudiante por nombre")

# Función que calcula el promedio de una lista de notas

def calcular_promedio(lista_notas):
    if len(lista_notas) == 0:
        return None
    return sum(lista_notas) / len(lista_notas)

# Función principal del programa

def main():
    estudiantes = []  # Lista para almacenar los datos de los estudiantes

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        # Opción 1: Agregar estudiante

        if opcion == "1":
            nombre = input("Nombre del estudiante: ")
            print("Tipo de dato del nombre:", type(nombre))

            # Solicita cuántas notas se van a ingresar

            while True:
                try:
                    cantidad_notas = int(input("¿Cuántas notas vas a ingresar?: "))
                    if cantidad_notas > 0:
                        break
                    else:
                        print("Debe ser un número mayor que cero.")
                except ValueError:
                    print("Por favor, ingresa un número válido.")

            notas = []

            # Bucle para ingresar cada nota con validación

            for i in range(cantidad_notas):
                while True:
                    try:
                        nota = float(input(f"Ingrese la nota {i+1}: "))
                        if 0 <= nota <= 10:
                            notas.append(nota)
                            print(f"Tipo de dato de la nota {i+1}:", type(nota))
                            break
                        else:
                            print("La nota debe estar entre 0 y 10.")
                    except ValueError:
                        print("Por favor, ingrese un número válido.")

            promedio = calcular_promedio(notas)
            print("Tipo de dato del promedio:", type(promedio))

            # Condición compuesta para aprobar

            aprobado = promedio >= 6.0 and all(n >= 4.0 for n in notas)
            print("Tipo de dato del estado de aprobación:", type(aprobado))

            # Diccionario con los datos del estudiante

            estudiante = {
                "nombre": nombre,
                "notas": notas,
                "promedio": promedio,
                "aprobado": aprobado
            }
            estudiantes.append(estudiante)
            print(f"\nEstudiante {nombre} agregado correctamente.")

        # Opción 2: Mostrar todos los estudiantes

        elif opcion == "2":
            print("\n" + "=" * 30)
            print("\tLISTA DE ESTUDIANTES")
            print("=" * 30)
            aprobados = 0
            reprobados = 0
            for est in estudiantes:
                estado = "Aprobado" if est["aprobado"] else "Reprobado"
                if est["aprobado"]:
                    aprobados += 1
                else:
                    reprobados += 1
                primeras_dos = est["notas"][:2]  # Slicing para mostrar solo las dos primeras notas
                print(f"{est['nombre']}\tPromedio: {est['promedio']:.2f}\t{estado}\tNotas: {primeras_dos}")
            print("-" * 30)
            print(f"Resumen:\t{aprobados} Aprobado(s)\t{reprobados} Reprobado(s)")

        # Opción 3: Salir del programa

        elif opcion == "3":
            print("¡Hasta luego!")
            break

        # Opción 4: Eliminar estudiante por nombre

        elif opcion == "4":
            nombre_eliminar = input("Nombre del estudiante a eliminar: ")
            encontrado = False
            for est in estudiantes:
                if est["nombre"].lower() == nombre_eliminar.lower():
                    estudiantes.remove(est)
                    print(f"Estudiante {nombre_eliminar} eliminado correctamente.")
                    encontrado = True
                    break
            if not encontrado:
                print(f"No se encontró al estudiante con nombre '{nombre_eliminar}'.")

        # Opción 5: Buscar estudiante por nombre

        elif opcion == "5":
            nombre_buscar = input("Nombre del estudiante a buscar: ")
            encontrado = False
            for est in estudiantes:
                if est["nombre"].lower() == nombre_buscar.lower():
                    estado = "Aprobado" if est["aprobado"] else "Reprobado"
                    print("\n" + "=" * 30)
                    print(f"Estudiante: {est['nombre']}")
                    print(f"Notas: {est['notas']}")
                    print(f"Promedio: {est['promedio']:.2f}")
                    print(f"Estado: {estado}")
                    print("=" * 30)
                    encontrado = True
                    break
            if not encontrado:
                print(f"No se encontró al estudiante con nombre '{nombre_buscar}'.")

        # Opción inválida
        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutar el programa
main()


