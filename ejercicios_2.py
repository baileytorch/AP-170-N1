# Convertidor de unidades de T°
# Fahrenheit, Celsius, Kelvin

# 1.- Generar menú para hacer conversiones
# 2.- En base al menu, seleccionar opciones y solicitar datos al usuario
# 3.- Realizar la conversión solicitada

# Fahrenheit a Celsius => (°F - 32) x 5/9
# Celsius a Fahrenheit => (°C x 9/5) + 32
# Celsius a Kelvin => (°C) + 273
# Kelvin a Celsius => (°K) - 273

def menu():
    print()
    print("[1] Convertir Celsius a Fahrenheit.")
    print("[2] Convertir Celsius a Kelvin.")
    print("[3] Convertir Fahrenheit a Celsius.")
    print("[4] Convertir Fahrenheit a Kelvin.")
    print("[5] Convertir Kelvin a Celsius.")
    print("[6] Convertir Kelvin a Fahrenheit.")
    print("[0] Salir.")
    
def convertir_celsius_fahrenheit(temperatura):
    fahrenheit = (temperatura * 9/5) + 32
    return fahrenheit

def convertir_celsius_kelvin(temperatura):
    kelvin = temperatura + 273
    return kelvin

def convertir_fahrenheit_celsius(temperatura):
    celsius = (temperatura - 32) * 5/9
    return celsius

def convertir_fehrenheit_kelvin(temperatura):
    celsius = convertir_fahrenheit_celsius(temperatura)
    kelvin = convertir_celsius_kelvin(celsius)
    return kelvin

def convertir_kelvin_celsius(temperatura):
    celsius = temperatura - 273
    return celsius

def convertir_kelvin_fahrenheit(temperatura):
    celsius = convertir_kelvin_celsius(temperatura)
    fahrenheit = convertir_celsius_fahrenheit(celsius)
    return fahrenheit

def solicitar_datos():    
    tempratura_inicial = float(input("Ingrese su Temperatura: "))
    return tempratura_inicial

def error_opcion():
    print('INGRESA UNA OPCIÓN VÁLIDA.')

def principal():    
    print("Súper Conversor de Temperaturas Python!!")
    print("========================================")
    while True:
        try:
            menu()
            opcion = input("Seleccione su Opción [0-6]: ")
            temperatura_inicial = 0
            temperatura_final = 0
            escala_inicial = ""
            escala_final = ""
            
            if opcion == "1":
                temperatura_inicial = solicitar_datos()
                temperatura_final = convertir_celsius_fahrenheit(temperatura_inicial)
                escala_inicial = "°C"
                escala_final = "°F"
            elif opcion == "2":
                temperatura_inicial = solicitar_datos()
                temperatura_final = convertir_celsius_kelvin(temperatura_inicial)
                escala_inicial = "°C"
                escala_final = "°K"
            elif opcion == "3":
                temperatura_inicial = solicitar_datos()
                temperatura_final = convertir_fahrenheit_celsius(temperatura_inicial)
                escala_inicial = "°F"
                escala_final = "°C"
            elif opcion == "4":
                temperatura_inicial = solicitar_datos()
                temperatura_final = convertir_fehrenheit_kelvin(temperatura_inicial)
                escala_inicial = "°F"
                escala_final = "°K"
            elif opcion == "5":
                temperatura_inicial = solicitar_datos()
                temperatura_final = convertir_kelvin_celsius(temperatura_inicial)
                escala_inicial = "°K"
                escala_final = "°C"
            elif opcion == "6":
                temperatura_inicial = solicitar_datos()
                temperatura_final = convertir_kelvin_fahrenheit(temperatura_inicial)
                escala_inicial = "°K"
                escala_final = "°F"
            elif opcion == "0":
                print("Saliendo...")
                break
            else:
                error_opcion()
        except ValueError:
            error_opcion()
        
        print()
        print(f"{temperatura_inicial}{escala_inicial} = {temperatura_final}{escala_final}")

principal()
    