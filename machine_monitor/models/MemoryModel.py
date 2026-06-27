from dataclasses import dataclass
import wmi


@dataclass(frozen=True)
class MemoryInfo:
    fabricant: str
    capacidade: int 
    velocidade: int
    part_number: str

    def to_display_lines(self) -> list[str]:
        return [
            f"Fabricante: {self.fabricant}",
            f"Capacidade: {self.capacidade // (1024**3)} GB",
            f"Velocidade: {self.velocidade} MHz",
            f"Número de peça: {self.part_number}",
        ]