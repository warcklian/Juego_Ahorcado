from ahorcado_diagramas import AhorcadoDiagramas
from palabras import obtener_palabra

class Ahorcado:
    def __init__(self):
        self.diagramas = AhorcadoDiagramas()
        self.palabra = obtener_palabra()  # Obtiene una palabra aleatoria
        self.intentos = len(self.diagramas.diagramas) - 1
        self.letras_adivinadas = []
        self.letras_erradas = []
        self.aciertos = ["_" for _ in self.palabra]

    def mostrar_estado(self):
        print("\n" + self.diagramas.obtener_diagrama(len(self.letras_erradas)))
        print("Palabra: " + " ".join(self.aciertos))
        print(f"Letras erradas: {', '.join(self.letras_erradas)}")
        print(f"Intentos restantes: {self.intentos - len(self.letras_erradas)}\n")

    def jugar(self):
        print("¡Bienvenido al juego del Ahorcado!")
        while len(self.letras_erradas) < self.intentos and "_" in self.aciertos:
            self.mostrar_estado()
            letra = input("Introduce una letra: ").lower()

            if not letra.isalpha() or len(letra) != 1:
                print("Por favor, ingresa solo una letra.")
                continue

            if letra in self.letras_adivinadas or letra in self.letras_erradas:
                print("Ya intentaste esta letra. Intenta con otra.")
                continue

            if letra in self.palabra:
                print("¡Correcto!")
                for i, char in enumerate(self.palabra):
                    if char == letra:
                        self.aciertos[i] = letra
                self.letras_adivinadas.append(letra)
            else:
                print("Incorrecto. Pierdes un intento.")
                self.letras_erradas.append(letra)

        if "_" not in self.aciertos:
            print(f"¡Felicidades! Has adivinado la palabra: {self.palabra}")
        else:
            self.mostrar_estado()
            print("¡Oh no! Te has quedado sin intentos.")
            print(f"La palabra era: {self.palabra}")

if __name__ == "__main__":
    juego = Ahorcado()
    juego.jugar()
