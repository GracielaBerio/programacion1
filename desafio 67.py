# Desafío 67

def dividir_numeros():
    """
    Se solicitan dos números enteros al usuario para realizar la división.
    Las excepcionesson utilizdas para los valores no numéricos y división por cero, u otra exceptión
    """
    while True:
        try:
            # Se solicita al usuario que ingrese dos números enteros.
            num1 = int(input("Introduce el primer número (dividendo): "))
            num2 = int(input("Introduce el segundo número (divisor): "))

            # Realiza la división.
            resultado = num1 / num2
            
            # Imprime el resultado si la división es exitosa.
            print(f"\nEl resultado de la división es: {resultado}")
            break  # Sale del bucle si no hay errores.

        except ValueError:
            # Captura y maneja la excepción si la entrada no es un número entero.
            print("\nError: Por favor, asegúrate de introducir solo números enteros.")
            print("---")
        
        except ZeroDivisionError:
            # Captura y maneja la excepción si el segundo número es cero.
            print("\nError: No se puede dividir un número entre cero.")
            print("---")
        
        except Exception as e:
            # Captura cualquier otra excepción inesperada.
            print(f"\nOcurrió un error inesperado: {e}")
            print("---")

# Llama a la función principal para ejecutar el programa.
dividir_numeros()


 except ValueError:
            print("\n Error: Por favor, introduce solo números enteros.")
