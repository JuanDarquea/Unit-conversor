#from distance import convert_distance # Importar la función de conversión de distancia
#from weight import convert_weight # Importar la función de conversión de peso
#from temperature import convert_temperature # Importar la función de conversión de temperatura
#from time import convert_time # Importar la función de conversión de temperatura y tiempo


def convert_distance(): # Función para convertir distancias
    print("\n=== CONVERSIÓN DE DISTANCIA ===")
    print("Seleccione la unidad de origen:")
    unidades = {
        "1": "metros",
        "2": "centímetros", 
        "3": "kilómetros",
        "4": "millas",
        "5": "pulgadas",
        "6": "pies",
        "7": "yardas"
    }
    for clave, valor in unidades.items():
        print(f"{clave}. {valor}")
    
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