#from distance import convert_distance # Importar la función de conversión de distancia
#from weight import convert_weight # Importar la función de conversión de peso
#from temperature import convert_temperature # Importar la función de conversión de temperatura
#from time import convert_time # Importar la función de conversión de temperatura y tiempo


def convert_distance(): # Función para convertir distancias
    print("\n=== CONVERSIÓN DE DISTANCIA ===")
    print("Seleccione la unidad de origen y destino para la conversión.") # Mostrar mensaje de selección de unidades
    # Definir un diccionario con las unidades de distancia y sus equivalencias
    unidades = {
        "1": "metros",
        "2": "centímetros", 
        "3": "kilómetros",
        "4": "millas",
        "5": "pulgadas",
        "6": "pies",
        "7": "yardas"
    }
    print("\nUnidades disponibles:")
    for clave, valor in unidades.items(): # Iterar sobre el diccionario de unidades y mostrar las opciones
        print(f"{clave}. {valor}") # Mostrar las opciones de unidades disponibles

    origen = input("\nIngrese el número de la unidad de origen: ") # Solicitar al usuario que ingrese la unidad de origen
    if origen not in unidades: # Comprobar si la unidad de origen es válida
        print("Unidad de origen no válida.")
        return # Salir de la función si la unidad de origen no es válida

    destino = input("Ingrese el número de la unidad de destino: ") # Solicitar al usuario que ingrese la unidad de destino
    if destino not in unidades: # Comprobar si la unidad de destino es válida
        print("Unidad de destino no válida.")
        return # Salir de la función si la unidad de destino no es válida

    valor = float(input("Ingrese el valor a convertir: ")) # Solicitar al usuario que ingrese el valor a convertir
    # Realizar la conversión (aquí se debe implementar la lógica de conversión)
    print(f"\nConvirtiendo {valor} {unidades[origen]} a {unidades[destino]}...")

    # Aquí se debe implementar la lógica de conversión entre las unidades seleccionadas
    # Por ejemplo, si origen es "1" (metros) y destino es "2" (centímetros), se puede hacer:
    if origen == "1" and destino == "2": # Si la unidad de origen es metros y la unidad de destino es centímetros
        resultado = valor * 100 # Convertir metros a centímetros
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("Conversión finalizada.")
            return
    elif origen == "1" and destino == "3": # Si la unidad de origen es metros y la unidad de destino es kilómetros
        resultado = valor / 1000 # Convertir metros a kilómetros
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("Conversión finalizada.")
            return
    elif origen == "1" and destino == "4": # Si la unidad de origen es metros y la unidad de destino es millas
        resultado = valor / 1609.34 # Convertir metros a millas
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("Conversión finalizada.")
            return
    elif origen == "1" and destino == "5": # Si la unidad de origen es metros y la unidad de destino es pulgadas
        resultado = valor * 39.3701 # Convertir metros a pulgadas
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("Conversión finalizada.")
            return
    elif origen == "1" and destino == "6": # Si la unidad de origen es metros y la unidad de destino es pies
        resultado = valor * 3.28084 # Convertir metros a pies
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("Conversión finalizada.")
            return
    elif origen == "1" and destino == "7": # Si la unidad de origen es metros y la unidad de destino es yardas
        resultado = valor * 1.09361 # Convertir metros a yardas
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("Conversión finalizada.")
            return
    elif origen == "2" and destino == "1": # Si la unidad de origen es centímetros y la unidad de destino es metros
        resultado = valor / 100 # Convertir centímetros a metros
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("Conversión finalizada.")
            return
    elif origen == "2" and destino == "3": # Si la unidad de origen es centímetros y la unidad de destino es kilómetros
        resultado = valor / 100000 # Convertir centímetros a kilómetros
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("Conversión finalizada.")
            return
    elif origen == "2" and destino == "4": # Si la unidad de origen es centímetros y la unidad de destino es millas
        resultado = valor / 160934 # Convertir centímetros a millas
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("Conversión finalizada.")
            return
    elif origen == "2" and destino == "5": # Si la unidad de origen es centímetros y la unidad de destino es pulgadas
        resultado = valor / 2.54 # Convertir centímetros a pulgadas
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("Conversión finalizada.")
            return
    elif origen == "2" and destino == "6": # Si la unidad de origen es centímetros y la unidad de destino es pies
        resultado = valor / 30.48 # Convertir centímetros a pies
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("Conversión finalizada.")
            return
    elif origen == "2" and destino == "7": # Si la unidad de origen es centímetros y la unidad de destino es yardas
        resultado = valor / 91.44 # Convertir centímetros a yardas
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("Conversión finalizada.")
            return
    elif origen == "3" and destino == "1": # Si la unidad de origen es kilómetros y la unidad de destino es metros
        resultado = valor * 1000 # Convertir kilómetros a metros
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("Conversión finalizada.")
            return
    elif origen == "3" and destino == "2": # Si la unidad de origen es kilómetros y la unidad de destino es centímetros
        resultado = valor * 100000 # Convertir kilómetros a centímetros
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("Conversión finalizada.")
            return
    elif origen == "3" and destino == "4": # Si la unidad de origen es kilómetros y la unidad de destino es millas
        resultado = valor / 1.60934 # Convertir kilómetros a millas
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("Conversión finalizada.")
            return
    elif origen == "3" and destino == "5": # Si la unidad de origen es kilómetros y la unidad de destino es pulgadas
        resultado = valor * 39370.1 # Convertir kilómetros a pulgadas
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("Conversión finalizada.")
            return
    elif origen == "3" and destino == "6": # Si la unidad de origen es kilómetros y la unidad de destino es pies
        resultado = valor * 3280.84 # Convertir kilómetros a pies
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("Conversión finalizada.")
            return
    elif origen == "3" and destino == "7": # Si la unidad de origen es kilómetros y la unidad de destino es yardas
        resultado = valor * 1093.61 # Convertir kilómetros a yardas
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("Conversión finalizada.")
            return
    elif origen == "4" and destino == "1": # Si la unidad de origen es millas y la unidad de destino es metros
        resultado = valor * 1609.34 # Convertir millas a metros
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("Conversión finalizada.")
            return
    elif origen == "4" and destino == "2": # Si la unidad de origen es millas y la unidad de destino es centímetros
        resultado = valor * 160934 # Convertir millas a centímetros
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("Conversión finalizada.")
            return
    elif origen == "4" and destino == "3": # Si la unidad de origen es millas y la unidad de destino es kilómetros
        resultado = valor * 1.60934 # Convertir millas a kilómetros
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("Conversión finalizada.")
            return
    elif origen == "4" and destino == "5": # Si la unidad de origen es millas y la unidad de destino es pulgadas
        resultado = valor * 63360 # Convertir millas a pulgadas
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("Conversión finalizada.")
            return
    elif origen == "4" and destino == "6": # Si la unidad de origen es millas y la unidad de destino es pies
        resultado = valor * 5280 # Convertir millas a pies
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("Conversión finalizada.")
            return
    elif origen == "4" and destino == "7": # Si la unidad de origen es millas y la unidad de destino es yardas
        resultado = valor * 1760 # Convertir millas a yardas
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("Conversión finalizada.")
            return
    elif origen == "5" and destino == "1": # Si la unidad de origen es pulgadas y la unidad de destino es metros
        resultado = valor / 39.3701 # Convertir pulgadas a metros
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("Conversión finalizada.")
            return
    elif origen == "5" and destino == "2": # Si la unidad de origen es pulgadas y la unidad de destino es centímetros
        resultado = valor * 2.54 # Convertir pulgadas a centímetros
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("Conversión finalizada.")
            return
    elif origen == "5" and destino == "3": # Si la unidad de origen es pulgadas y la unidad de destino es kilómetros
        resultado = valor / 39370.1 # Convertir pulgadas a kilómetros
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("Conversión finalizada.")
            return
    elif origen == "5" and destino == "4": # Si la unidad de origen es pulgadas y la unidad de destino es millas
        resultado = valor / 63360 # Convertir pulgadas a millas
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("Conversión finalizada.")
            return
    elif origen == "5" and destino == "6": # Si la unidad de origen es pulgadas y la unidad de destino es pies
        resultado = valor / 12 # Convertir pulgadas a pies
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("Conversión finalizada.")
            return
    elif origen == "5" and destino == "7": # Si la unidad de origen es pulgadas y la unidad de destino es yardas
        resultado = valor / 36 # Convertir pulgadas a yardas
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("Conversión finalizada.")
            return
    elif origen == "6" and destino == "1": # Si la unidad de origen es pies y la unidad de destino es metros
        resultado = valor / 3.28084 # Convertir pies a metros
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("Conversión finalizada.")
            return
    elif origen == "6" and destino == "2": # Si la unidad de origen es pies y la unidad de destino es centímetros
        resultado = valor * 30.48 # Convertir pies a centímetros
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("Conversión finalizada.")
            return
    elif origen == "6" and destino == "3": # Si la unidad de origen es pies y la unidad de destino es kilómetros
        resultado = valor / 3280.84 # Convertir pies a kilómetros
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("Conversión finalizada.")
            return
    elif origen == "6" and destino == "4": # Si la unidad de origen es pies y la unidad de destino es millas
        resultado = valor / 5280 # Convertir pies a millas
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("Conversión finalizada.")
            return
    elif origen == "6" and destino == "5": # Si la unidad de origen es pies y la unidad de destino es pulgadas
        resultado = valor * 12 # Convertir pies a pulgadas
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("Conversión finalizada.")
            return
    elif origen == "6" and destino == "7": # Si la unidad de origen es pies y la unidad de destino es yardas
        resultado = valor / 3 # Convertir pies a yardas
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("Conversión finalizada.")
            return
    elif origen == "7" and destino == "1": # Si la unidad de origen es yardas y la unidad de destino es metros
        resultado = valor / 1.09361 # Convertir yardas a metros
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("Conversión finalizada.")
            return
    elif origen == "7" and destino == "2": # Si la unidad de origen es yardas y la unidad de destino es centímetros
        resultado = valor * 91.44 # Convertir yardas a centímetros
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("Conversión finalizada.")
            return
    elif origen == "7" and destino == "3": # Si la unidad de origen es yardas y la unidad de destino es kilómetros
        resultado = valor / 1093.61 # Convertir yardas a kilómetros
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("Conversión finalizada.")
            return
    elif origen == "7" and destino == "4": # Si la unidad de origen es yardas y la unidad de destino es millas
        resultado = valor / 1760 # Convertir yardas a millas
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("Conversión finalizada.")
            return
    elif origen == "7" and destino == "5": # Si la unidad de origen es yardas y la unidad de destino es pulgadas
        resultado = valor * 36  # Convertir yardas a pulgadas
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("Conversión finalizada.")
            return
    elif origen == "7" and destino == "6": # Si la unidad de origen es yardas y la unidad de destino es pies
        resultado = valor * 3 # Convertir yardas a pies
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("Conversión finalizada.")
            return
    else:
        print("Conversión no implementada para estas unidades.")
        return convert_distance() # Salir de la función si la conversión no está implementada
    

def mostrar_menu(): # Función para mostrar el menú de opciones
    # Mostrar el menú de opciones
    print("=== CONVERSOR DE UNIDADES ===")
    print("1. Distancia")
    print("2. Peso")
    print("3. Temperatura") 
    print("4. Tiempo")
    print("5. Salir")
    choice = input("\nSeleccione una opción (1-5): ")
    return choice # Devolver la opción seleccionada

def main(): # Función principal del programa
    # Importar las funciones de conversión
    while True: # Bucle infinito para mantener el programa en ejecución    
        choice = mostrar_menu() # Llamar a la función para mostrar el menú y obtener la opción seleccionada
        # Comprobar la opción seleccionada y llamar a la función correspondiente
        if choice == "1":
            convert_distance()
        elif choice == "2":
            print("convert_weight()")
        elif choice == "3":
            print("convert_temperature()")
        elif choice == "4":
            print("convert_time()")
        elif choice == "5":
            print("\nSaliendo del programa. ¡Hasta luego!")
            break
        else:
            print("\nOpción no válida. Por favor, seleccione una opción del 1 al 5.")

if __name__ == "__main__": # Comprobar si el script se está ejecutando directamente
    main() # Llamar a la función principal
