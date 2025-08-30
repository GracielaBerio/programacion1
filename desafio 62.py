# Desafio 62

# Clase Músico

class Musico:
    def instrumento(self):
        return "El músico toca algún instrumento"

# Subclase Guitarrista
class Guitarrista(Musico):
    def instrumento(self):
        return "El guitarrista toca la guitarra"

# Subclase Baterista
class Baterista(Musico):
    def instrumento(self):
        return "El baterista toca la batería"

# Demostración de polimorfismo
def mostrar_instrumento(musico):
    print(musico.instrumento())

# Aquí se crean los objetos
guitarrista = Guitarrista()
baterista = Baterista()

# Aquí se usar la función polimórfica
mostrar_instrumento(guitarrista)
mostrar_instrumento(baterista)

# Fundamentación
# Se hace la clase Musico y dos hijas (Guitarrista y Baterista) 
# para que cada uno toque su instrumento. Llamando al mismo método, cada objeto responde distinto.