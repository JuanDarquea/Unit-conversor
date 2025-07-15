#from distance import convert_distance # Importar la función de conversión de distancia
#from weight import convert_weight # Importar la función de conversión de peso
#from temperature import convert_temperature # Importar la función de conversión de temperatura
#from time import convert_time # Importar la función de conversión de temperatura y tiempo
import os

# Función para limpiar la pantalla
def clear_screen():
    # Para Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # Para Mac y Linux
    else:
        _ = os.system('clear')

def convert_distance(): # Función para convertir distancias
    clear_screen() # Limpiar la pantalla al inicio de la función
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
        print("¡UNIDAD DE ORIGEN NO VALIDA!")
        return convert_distance() # Salir de la función si la unidad de origen no es válida

    destino = input("Ingrese el número de la unidad de destino: ") # Solicitar al usuario que ingrese la unidad de destino
    if destino not in unidades: # Comprobar si la unidad de destino es válida
        print("¡UNIDAD DE DESTINO NO VALIDA!")
        return convert_distance() # Salir de la función si la unidad de destino no es válida

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
            print("\nConversión finalizada.")
            return
    elif origen == "1" and destino == "3": # Si la unidad de origen es metros y la unidad de destino es kilómetros
        resultado = valor / 1000 # Convertir metros a kilómetros
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("\nConversión finalizada.")
            return
    elif origen == "1" and destino == "4": # Si la unidad de origen es metros y la unidad de destino es millas
        resultado = valor / 1609.34 # Convertir metros a millas
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("\nConversión finalizada.")
            return
    elif origen == "1" and destino == "5": # Si la unidad de origen es metros y la unidad de destino es pulgadas
        resultado = valor * 39.3701 # Convertir metros a pulgadas
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("\nConversión finalizada.")
            return
    elif origen == "1" and destino == "6": # Si la unidad de origen es metros y la unidad de destino es pies
        resultado = valor * 3.28084 # Convertir metros a pies
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("\nConversión finalizada.")
            return
    elif origen == "1" and destino == "7": # Si la unidad de origen es metros y la unidad de destino es yardas
        resultado = valor * 1.09361 # Convertir metros a yardas
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("\nConversión finalizada.")
            return
    elif origen == "2" and destino == "1": # Si la unidad de origen es centímetros y la unidad de destino es metros
        resultado = valor / 100 # Convertir centímetros a metros
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("\nConversión finalizada.")
            return
    elif origen == "2" and destino == "3": # Si la unidad de origen es centímetros y la unidad de destino es kilómetros
        resultado = valor / 100000 # Convertir centímetros a kilómetros
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("\nConversión finalizada.")
            return
    elif origen == "2" and destino == "4": # Si la unidad de origen es centímetros y la unidad de destino es millas
        resultado = valor / 160934 # Convertir centímetros a millas
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("\nConversión finalizada.")
            return
    elif origen == "2" and destino == "5": # Si la unidad de origen es centímetros y la unidad de destino es pulgadas
        resultado = valor / 2.54 # Convertir centímetros a pulgadas
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("\nConversión finalizada.")
            return
    elif origen == "2" and destino == "6": # Si la unidad de origen es centímetros y la unidad de destino es pies
        resultado = valor / 30.48 # Convertir centímetros a pies
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("\nConversión finalizada.")
            return
    elif origen == "2" and destino == "7": # Si la unidad de origen es centímetros y la unidad de destino es yardas
        resultado = valor / 91.44 # Convertir centímetros a yardas
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("\nConversión finalizada.")
            return
    elif origen == "3" and destino == "1": # Si la unidad de origen es kilómetros y la unidad de destino es metros
        resultado = valor * 1000 # Convertir kilómetros a metros
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("\nConversión finalizada.")
            return
    elif origen == "3" and destino == "2": # Si la unidad de origen es kilómetros y la unidad de destino es centímetros
        resultado = valor * 100000 # Convertir kilómetros a centímetros
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("\nConversión finalizada.")
            return
    elif origen == "3" and destino == "4": # Si la unidad de origen es kilómetros y la unidad de destino es millas
        resultado = valor / 1.60934 # Convertir kilómetros a millas
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("\nConversión finalizada.")
            return
    elif origen == "3" and destino == "5": # Si la unidad de origen es kilómetros y la unidad de destino es pulgadas
        resultado = valor * 39370.1 # Convertir kilómetros a pulgadas
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("\nConversión finalizada.")
            return
    elif origen == "3" and destino == "6": # Si la unidad de origen es kilómetros y la unidad de destino es pies
        resultado = valor * 3280.84 # Convertir kilómetros a pies
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("\nConversión finalizada.")
            return
    elif origen == "3" and destino == "7": # Si la unidad de origen es kilómetros y la unidad de destino es yardas
        resultado = valor * 1093.61 # Convertir kilómetros a yardas
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("\nConversión finalizada.")
            return
    elif origen == "4" and destino == "1": # Si la unidad de origen es millas y la unidad de destino es metros
        resultado = valor * 1609.34 # Convertir millas a metros
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("\nConversión finalizada.")
            return
    elif origen == "4" and destino == "2": # Si la unidad de origen es millas y la unidad de destino es centímetros
        resultado = valor * 160934 # Convertir millas a centímetros
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("\nConversión finalizada.")
            return
    elif origen == "4" and destino == "3": # Si la unidad de origen es millas y la unidad de destino es kilómetros
        resultado = valor * 1.60934 # Convertir millas a kilómetros
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("\nConversión finalizada.")
            return
    elif origen == "4" and destino == "5": # Si la unidad de origen es millas y la unidad de destino es pulgadas
        resultado = valor * 63360 # Convertir millas a pulgadas
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("\nConversión finalizada.")
            return
    elif origen == "4" and destino == "6": # Si la unidad de origen es millas y la unidad de destino es pies
        resultado = valor * 5280 # Convertir millas a pies
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("\nConversión finalizada.")
            return
    elif origen == "4" and destino == "7": # Si la unidad de origen es millas y la unidad de destino es yardas
        resultado = valor * 1760 # Convertir millas a yardas
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("\nConversión finalizada.")
            return
    elif origen == "5" and destino == "1": # Si la unidad de origen es pulgadas y la unidad de destino es metros
        resultado = valor / 39.3701 # Convertir pulgadas a metros
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("\nConversión finalizada.")
            return
    elif origen == "5" and destino == "2": # Si la unidad de origen es pulgadas y la unidad de destino es centímetros
        resultado = valor * 2.54 # Convertir pulgadas a centímetros
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("\nConversión finalizada.")
            return
    elif origen == "5" and destino == "3": # Si la unidad de origen es pulgadas y la unidad de destino es kilómetros
        resultado = valor / 39370.1 # Convertir pulgadas a kilómetros
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("\nConversión finalizada.")
            return
    elif origen == "5" and destino == "4": # Si la unidad de origen es pulgadas y la unidad de destino es millas
        resultado = valor / 63360 # Convertir pulgadas a millas
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("\nConversión finalizada.")
            return
    elif origen == "5" and destino == "6": # Si la unidad de origen es pulgadas y la unidad de destino es pies
        resultado = valor / 12 # Convertir pulgadas a pies
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("\nConversión finalizada.")
            return
    elif origen == "5" and destino == "7": # Si la unidad de origen es pulgadas y la unidad de destino es yardas
        resultado = valor / 36 # Convertir pulgadas a yardas
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("\nConversión finalizada.")
            return
    elif origen == "6" and destino == "1": # Si la unidad de origen es pies y la unidad de destino es metros
        resultado = valor / 3.28084 # Convertir pies a metros
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("\nConversión finalizada.")
            return
    elif origen == "6" and destino == "2": # Si la unidad de origen es pies y la unidad de destino es centímetros
        resultado = valor * 30.48 # Convertir pies a centímetros
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("\nConversión finalizada.")
            return
    elif origen == "6" and destino == "3": # Si la unidad de origen es pies y la unidad de destino es kilómetros
        resultado = valor / 3280.84 # Convertir pies a kilómetros
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("\nConversión finalizada.")
            return
    elif origen == "6" and destino == "4": # Si la unidad de origen es pies y la unidad de destino es millas
        resultado = valor / 5280 # Convertir pies a millas
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("\nConversión finalizada.")
            return
    elif origen == "6" and destino == "5": # Si la unidad de origen es pies y la unidad de destino es pulgadas
        resultado = valor * 12 # Convertir pies a pulgadas
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("\nConversión finalizada.")
            return
    elif origen == "6" and destino == "7": # Si la unidad de origen es pies y la unidad de destino es yardas
        resultado = valor / 3 # Convertir pies a yardas
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("\nConversión finalizada.")
            return
    elif origen == "7" and destino == "1": # Si la unidad de origen es yardas y la unidad de destino es metros
        resultado = valor / 1.09361 # Convertir yardas a metros
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("\nConversión finalizada.")
            return
    elif origen == "7" and destino == "2": # Si la unidad de origen es yardas y la unidad de destino es centímetros
        resultado = valor * 91.44 # Convertir yardas a centímetros
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("\nConversión finalizada.")
            return
    elif origen == "7" and destino == "3": # Si la unidad de origen es yardas y la unidad de destino es kilómetros
        resultado = valor / 1093.61 # Convertir yardas a kilómetros
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("\nConversión finalizada.")
            return
    elif origen == "7" and destino == "4": # Si la unidad de origen es yardas y la unidad de destino es millas
        resultado = valor / 1760 # Convertir yardas a millas
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("\nConversión finalizada.")
            return
    elif origen == "7" and destino == "5": # Si la unidad de origen es yardas y la unidad de destino es pulgadas
        resultado = valor * 36  # Convertir yardas a pulgadas
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("\nConversión finalizada.")
            return
    elif origen == "7" and destino == "6": # Si la unidad de origen es yardas y la unidad de destino es pies
        resultado = valor * 3 # Convertir yardas a pies
        print(f"Resultado: {resultado} {unidades[destino]}")
        print("\n¿Desea realizar otra conversión de distancia? (s/n)")
        otra_conversion = input().lower() # Preguntar al usuario si desea realizar otra conversión
        if otra_conversion == "s":
            return convert_distance()
        else:
            print("\nConversión finalizada.")
            return
    else:
        print("Conversión no implementada para estas unidades.")
        return convert_distance() # Salir de la función si la conversión no está implementada
    
def convert_weight(): # Función para convertir pesos
    clear_screen() # Limpiar la pantalla al inicio de la función
    print("\n=== CONVERSIÓN DE PESO ===")
    print("Seleccione la unidad de origen y destino para la conversión.") # Mostrar mensaje de selección de unidades
    # Definir un diccionario con las unidades de peso y sus equivalencias
    unidades = {
        "1": "kilogramos",
        "2": "gramos",
        "3": "toneladas",
        "4": "libras",
        "5": "onzas"
    }
    print("\nUnidades disponibles:")
    for clave, valor in unidades.items(): # Iterar sobre el diccionario de unidades y mostrar las opciones
        print(f"{clave}. {valor}") # Mostrar las opciones de unidades disponibles

    origen = input("\nIngrese el número de la unidad de origen: ")
    if origen not in unidades:
        print("\n¡UNIDAD DE ORIGEN NO VALIDA!")
        return convert_weight()

    destino = input("Ingrese el número de la unidad de destino: ")
    if destino not in unidades:
        print("\n¡UNIDAD DE DESTINO NO VALIDA!")
        return convert_weight()

    valor = float(input("Ingrese el valor a convertir: "))
    print(f"\nConvirtiendo {valor} {unidades[origen]} a {unidades[destino]}...")

    # Realizar la conversión (aquí se debe implementar la lógica de conversión)
    if origen == destino:
        resultado = valor
    elif origen == "1" and destino == "2": # kg a g
        resultado = valor * 1000
    elif origen == "1" and destino == "3": # kg a t
        resultado = valor / 1000
    elif origen == "1" and destino == "4": # kg a lb
        resultado = valor * 2.20462
    elif origen == "1" and destino == "5": # kg a oz
        resultado = valor * 35.274
    elif origen == "2" and destino == "1": # g a kg
        resultado = valor / 1000
    elif origen == "2" and destino == "3": # g a t
        resultado = valor / 1_000_000
    elif origen == "2" and destino == "4": # g a lb
        resultado = valor / 453.592
    elif origen == "2" and destino == "5": # g a oz
        resultado = valor / 28.3495
    elif origen == "3" and destino == "1": # t a kg
        resultado = valor * 1000
    elif origen == "3" and destino == "2": # t a g
        resultado = valor * 1_000_000
    elif origen == "3" and destino == "4": # t a lb
        resultado = valor * 2204.62
    elif origen == "3" and destino == "5": # t a oz
        resultado = valor * 35274
    elif origen == "4" and destino == "1": # lb a kg
        resultado = valor / 2.20462
    elif origen == "4" and destino == "2": # lb a g
        resultado = valor * 453.592
    elif origen == "4" and destino == "3": # lb a t
        resultado = valor / 2204.62
    elif origen == "4" and destino == "5": # lb a oz
        resultado = valor * 16
    elif origen == "5" and destino == "1": # oz a kg
        resultado = valor / 35.274
    elif origen == "5" and destino == "2": # oz a g
        resultado = valor * 28.3495
    elif origen == "5" and destino == "3": # oz a t
        resultado = valor / 35274
    elif origen == "5" and destino == "4": # oz a lb
        resultado = valor / 16
    else:
        print("\nConversión no implementada para estas unidades.")
        return convert_weight()

    print(f"Resultado: {resultado} {unidades[destino]}")
    print("\n¿Desea realizar otra conversión de peso? (s/n)")
    otra_conversion = input().lower()
    if otra_conversion == "s":
        return convert_weight()
    else:
        print("\nConversión finalizada.")
        return

def convert_temperature(): #call temperature conversion function
    clear_screen() # Limpiar la pantalla al inicio de la función
    print("\n=== CONVERSIÓN DE TEMPERATURA ===")
    print("Seleccione la unidad de origen y destino para la conversión.") # Mostrar mensaje de selección de unidades
    # Definir un diccionario con las unidades de temperatura y sus equivalencias
    unidades = {
        "1": "Celsius",
        "2": "Fahrenheit",
        "3": "Kelvin"
    }

    print("\nUnidades disponibles:")
    for clave, valor in unidades.items(): # llama a las unidades de temperatura y muestra las opciones
        print(f"{clave}. {valor}") # muestra en pantalla las opciones de unidades disponibles

    origen = input("\nIngrese el número de la unidad de origen: ") # Solicitar al usuario que ingrese la unidad de origen
    if origen not in unidades: # en caso de que la unidad de origen no sea válida se presentará un mensaje
        print("\n¡El valor seleccionado no existe dentro de las opciones!")
        return convert_temperature() # Salir de la función si la unidad de origen no es válida
    destino = input("Ingrese el número de la unidad de destino: ") # Solicitar al usuario que ingrese la unidad de destino
    if destino not in unidades: 
        print("\n¡El valor seleccionado no existe dentro de las opciones!")
        return convert_temperature() # Salir de la función si la unidad de destino no es válida
    valor = float(input("Ingrese el valor a convertir: "))
    print(f"\nConvirtiendo {valor} {unidades[origen]} a {unidades[destino]}...")

    if origen == destino:
        resultado = valor
    elif origen == "1" and destino == "2": # Celsius a Farenheit
        resultado = (valor * (9/5)) + 32
    elif origen == "1" and destino == "3": # Celsius a Kelvin
        resultado = valor + 273.15
    elif origen == "2" and destino == "1": # Farenheit a Celsius
        resultado = (valor - 32) * (5/9)
    elif origen == "2" and destino == "3": # Farenheit a Kelvin
        resultado = (valor - 32) * (5/9) + 273.15
    elif origen == "3" and destino == "1": # Kelvin a Celsius
        resultado = valor - 273.15
    elif origen == "3" and destino == "2": # Kelvin a Farenheit
        resultado = (valor - 273.15) * (9/5) + 32
    else:
        print("\nConversión no implementada para estas unidades.")
        return convert_temperature() # Regresar a la función de conversión de temperatura
    print(f"Resultado: {resultado} {unidades[destino]}")
    print("\n¿Desea realizar otra conversión de temperatura? (s/n)")
    otra_conversion = input().lower() # Lower case para aceptar 's' o 'n'
    if otra_conversion == "s" or otra_conversion == "sí":
        return convert_temperature()
    else:
        print("\nConversión finalizada.")
        return

def convert_time(): # llamar a la función para calcular tiempo
    clear_screen() # Limpiar la pantalla al inicio de la función
    print("\n===CONVERSIÓN DE TIEMPO===")
    print("Seleccione la unidad de origen y destino para la conversión.")
    unidades = {
        "1":"Segundos",
        "2":"Minutos",
        "3":"Horas",
        "4":"Dias",
        "5":"Semanas",
        "6":"Meses",
        "7":"Años"
    }
    print("Unidades disponibles:")
    for clave, valor in unidades.items():
        print(f"{clave}.{valor}")
    origen = input("\nIngrese el número de la unidad de origen: ")
    if origen not in unidades:
        print("\n¡El valor seleccionado no existe dentro de las opciones!")
        return convert_temperature()
    destino = input("Ingrese el número de la unidad de destino: ")
    if destino not in unidades:
        print("\n¡El valor seleccionado no existe dentro de las opciones!")
        return convert_temperature()
    valor = float(input("Ingrese el valor a convertir: "))
    print(f"\nConvirtiendo {valor} {unidades[origen]} a {unidades[destino]}...")

    if origen == destino:
        resultado = valor
    elif origen == "1" and destino == "2": # Segundos a Minutos
        resultado = valor / 60
    elif origen == "1" and destino == "3": # Segundos a Horas
        resultado = valor / 3600
    elif origen == "1" and destino == "4": # Segundos a Días
        resultado = valor / 86400
    elif origen == "1" and destino == "5": # Segundos a Semanas
        resultado = valor / 604800
    elif origen == "1" and destino == "6": # Segundos a Meses
        resultado = valor / 2629800
    elif origen == "1" and destino == "7": # Segundos a Años
        resultado = valor / 31557600
    elif origen == "2" and destino == "1": # Minutos a Segundos
        resultado = valor * 60
    elif origen == "2" and destino == "3": # Minutos a Horas
        resultado = valor / 60
    elif origen == "2" and destino == "4": # Minutos a Días
        resultado = valor / 1440
    elif origen == "2" and destino == "5": # Minutos a Semanas
        resultado = valor / 10080
    elif origen == "2" and destino == "6": # Minutos a Meses
        resultado = valor / 43800
    elif origen == "2" and destino == "7": # Minutos a Años
        resultado = valor / 525600
    elif origen == "3" and destino == "1": # Horas a Segundos
        resultado = valor * 3600
    elif origen == "3" and destino == "2": # Horas a Minutos
        resultado = valor * 60
    elif origen == "3" and destino == "4": # Horas a Días
        resultado = valor / 24
    elif origen == "3" and destino == "5": # Horas a Semanas
        resultado = valor / 168
    elif origen == "3" and destino == "6": # Horas a Meses
        resultado = valor / 730
    elif origen == "3" and destino == "7": # Horas a Años
        resultado = valor / 8760
    elif origen == "4" and destino == "1": # Días a Segundos
        resultado = valor * 86400
    elif origen == "4" and destino == "2": # Días a Minutos
        resultado = valor * 1440
    elif origen == "4" and destino == "3": # Días a Horas
        resultado = valor * 24
    elif origen == "4" and destino == "5": # Días a Semanas
        resultado = valor / 7
    elif origen == "4" and destino == "6": # Días a Meses
        resultado = valor / 30.44
    elif origen == "4" and destino == "7": # Días a Años
        resultado = valor / 365.25
    elif origen == "5" and destino == "1": # Semanas a Segundos
        resultado = valor * 604800
    elif origen == "5" and destino == "2": # Semanas a Minutos
        resultado = valor * 10080
    elif origen == "5" and destino == "3": # Semanas a Horas
        resultado = valor * 168
    elif origen == "5" and destino == "4": # Semanas a Días
        resultado = valor * 7
    elif origen == "5" and destino == "6": # Semanas a Meses
        resultado = valor / 4.34524
    elif origen == "5" and destino == "7": # Semanas a Años
        resultado = valor / 52.1775
    elif origen == "6" and destino == "1": # Meses a Segundos
        resultado = valor * 2629800
    elif origen == "6" and destino == "2": # Meses a Minutos
        resultado = valor * 43800
    elif origen == "6" and destino == "3": # Meses a Horas
        resultado = valor * 730
    elif origen == "6" and destino == "4": # Meses a Días
        resultado = valor * 30.44
    elif origen == "6" and destino == "5": # Meses a Semanas
        resultado = valor * 4.34524
    elif origen == "6" and destino == "7": # Meses a Años
        resultado = valor / 12
    elif origen == "7" and destino == "1": # Años a Segundos
        resultado = valor * 31557600
    elif origen == "7" and destino == "2": # Años a Minutos
        resultado = valor * 525600
    elif origen == "7" and destino == "3": # Años a Horas
        resultado = valor * 8760
    elif origen == "7" and destino == "4": # Años a Días
        resultado = valor * 365.25
    elif origen == "7" and destino == "5": # Años a Semanas
        resultado = valor * 52.1775
    elif origen == "7" and destino == "6": # Años a Meses
        resultado = valor * 12
    else:
        print("\nConversión no implementada para estas unidades.")
        return convert_time() # Regresar a la función de conversión de tiempo
    print(f"Resultado: {resultado} {unidades[destino]}")
    print("\n¿Desea realizar otra conversión de tiempo? (s/n)")
    otra_conversion = input().lower() # Lower case para aceptar 's' o 'n'
    if otra_conversion == "s" or otra_conversion == "si":
        return convert_time()
    else:
        print("\nConversión finalizada.")
        return 

def mostrar_menu(): # Función para mostrar el menú de opciones
    clear_screen() # Limpiar la pantalla al inicio de la función
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
            convert_weight()
        elif choice == "3":
            convert_temperature()
        elif choice == "4":
            convert_time()
        elif choice == "5":
            print("\nSaliendo del programa. ¡Hasta luego!")
            break
        else:
            print("\nOpción no válida. Por favor, seleccione una opción del 1 al 5.")
            input("Presione Enter para continuar...")

if __name__ == "__main__": # Comprobar si el script se está ejecutando directamente
    main() # Llamar a la función principal
