class AhorcadoDiagramas:
    def __init__(self):
        self.diagramas = [
            """
               -----
               |   |
                   |
                   |
                   |
                   |
            --------
            """,
            """
               -----
               |   |
               O   |
                   |
                   |
                   |
            --------
            """,
            """
               -----
               |   |
               O   |
               |   |
                   |
                   |
            --------
            """,
            """
               -----
               |   |
               O   |
              /|   |
                   |
                   |
            --------
            """,
            """
               -----
               |   |
               O   |
              /|\\  |
                   |
                   |
            --------
            """,
            """
               -----
               |   |
               O   |
              /|\\  |
              /    |
                   |
            --------
            """,
            """
               -----
               |   |
               O   |
              /|\\  |
              / \\  |
                   |
            --------
            """
        ]

    def obtener_diagrama(self, errores):
        return self.diagramas[errores]
