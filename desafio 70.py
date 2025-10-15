#desafio 70
"""
Se creó una excepción personalizada para evitar números negativos al calcular raíces cuadradas, 
garantizando entradas válidas y manejo de errores.

"""
import math

# Definimos la excepción personalizada
class NegativeNumberError(Exception):
    """Excepción para cuando se ingresa un número negativo."""
    pass

def calcular_raiz_cuadrada():
    while True:
        try:
            num = float(input("Debe ingresar un número para calcular su raíz cuadrada: "))
            
            # Verificamos si el número es negativo
            if num < 0:
                raise NegativeNumberError("Error, no se puede calcular la raíz cuadrada de un número negativo.")
            
            # Calculamos la raíz cuadrada
            resultado = math.sqrt(num)
            print(f"La raíz cuadrada de {num} es {resultado}")
            break  
        
        except NegativeNumberError as e:
            print(f"Error: {e}. Intenta nuevamente.")
        
        except ValueError:
            print("Error: Debes ingresar un número válido. Intenta nuevamente.")

# Ejecutamos 
calcular_raiz_cuadrada()
