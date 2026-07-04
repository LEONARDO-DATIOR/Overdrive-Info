from dataclasses import dataclass

class MemoryInfo:
    __fabricant: str
    __capacidade: int
    __velocidade: int

    def __init__(self, fabricant: str, capacidade: int, velocidade: int):
        self.__fabricant = fabricant
        self.__capacidade = capacidade
        self.__velocidade = velocidade

    @property
    def fabricant(self):
        return self.__fabricant

    @property
    def capacidade(self):
        return self.__capacidade / (1024**3)

    @property
    def velocidade(self):
        return self.__velocidade

    @fabricant.setter
    def fabricant(self, value):
        self.__fabricant = value

    @capacidade.setter
    def capacidade(self, value):
        self.__capacidade = value

    @velocidade.setter
    def velocidade(self, value):
        self.__velocidade = value

    def to_display_lines(self) -> list[str]:
        return [
            f"Fabricante: {self.fabricant}",
            f"Capacidade: {self.capacidade:.2f} GB",
            f"Velocidade: {self.velocidade} MHz",
        ]