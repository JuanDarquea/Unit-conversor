# **🔄 Unit Converter (Python CLI)**
### A comprehensive command-line unit conversion tool that supports distance, weight, temperature, and time conversions. Perfect for students, engineers, and anyone who needs quick and accurate unit conversions in their daily work.

## **✨ Features**
   - 🏃♂️ Distance Conversion: Meters, centimeters, kilometers, miles, inches, feet, yards
   - ⚖️ Weight Conversion: Kilograms, grams, tons, pounds, ounces
   - 🌡️ Temperature Conversion: Celsius, Fahrenheit, Kelvin
   - ⏰ Time Conversion: Seconds, minutes, hours, days, weeks, months, years
   - 🖥️ Cross-platform: Works on Windows, Mac, and Linux
   - 🔄 Continuous Conversion: Option to perform multiple conversions in sequence
   - ✅ Input Validation: Handles invalid inputs gracefully
   - 🧹 Clean Interface: Auto-clears screen for better user experience

## **🛠️ Requirements**
   * Python 3.6+ (uses only standard library)
   * Compatible with Windows, macOS, and Linux

## **🚀 Usage**
- Run the program:
   - *In bash*
      * python Unit_conversor.py
- Select conversion type from the main menu:
  
=== CONVERSOR DE UNIDADES ===

1. Distancia
2. Peso
3. Temperatura
4. Tiempo
5. Salir
- Choose source and target units, then enter the value to convert.
- Get instant results with the option to perform additional conversions.

## **📊 Supported Conversions**
### Category	Units Available
* Distance:	Meters, Centimeters, Kilometers, Miles, Inches, Feet, Yards
* Weight:	Kilograms, Grams, Tons, Pounds, Ounces
* Temperature:	Celsius, Fahrenheit, Kelvin
* Time:	Seconds, Minutes, Hours, Days, Weeks, Months, Years

## 💡 Example Usage
**Distance Conversion:**

=== CONVERSIÓN DE DISTANCIA ===

Unidades disponibles:

1. metros
2. centímetros
3. kilómetros
4. millas
5. pulgadas
6. pies
7. yardas

Ingrese el número de la unidad de origen: 1

Ingrese el número de la unidad de destino: 3

Ingrese el valor a convertir: 1500

Resultado: 1.5 kilómetros


**Temperature Conversion:**

=== CONVERSIÓN DE TEMPERATURA ===

Unidades disponibles:

1. Celsius
2. Fahrenheit
3. Kelvin

Ingrese el número de la unidad de origen: 1

Ingrese el número de la unidad de destino: 2

Ingrese el valor a convertir: 25

Resultado: 77.0 Fahrenheit


## **🏗️ Code Structure**

Unit_conversor.py

├── clear_screen()           # Cross-platform screen clearing

├── convert_distance()       # Distance unit conversions

├── convert_weight()         # Weight unit conversions

├── convert_temperature()    # Temperature unit conversions

├── convert_time()           # Time unit conversions

├── mostrar_menu()          # Main menu display

└── main()                  # Program entry point

## **🔧 Key Features**
* Accurate Conversion Factors: Uses precise mathematical relationships between units
* Error Handling: Validates user input and provides helpful error messages
* Modular Design: Each conversion type is handled by a separate function
* User-Friendly: Clear prompts and confirmation for continued use
* Bi-directional: Converts between any two units in each category

## **🌟 Perfect for Learning**
### This project demonstrates:
* Function organization and modular programming
* Dictionary usage for mapping options
* Input validation and error handling
* Mathematical operations and conversion formulas
* User interface design for CLI applications
* Cross-platform compatibility considerations

## **🤝 Contributing**
### Feel free to contribute by:
* Adding new unit categories (volume, area, etc.)
* Improving the user interface
* Adding more conversion factors
* Translating to other languages
* Optimizing the code structure

## **📝 Notes**
Interface is currently in Spanish

All conversion factors are mathematically accurate

Program runs in a continuous loop until user chooses to exit

Screen clearing works across different operating systems

Happy Converting! 🎯

*Built by an aspiring data analyst and AI scientist for practical learning and everyday use.*
