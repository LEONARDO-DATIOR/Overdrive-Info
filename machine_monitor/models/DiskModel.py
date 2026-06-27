from dataclasses import dataclass

from machine_monitor.utils.utils import format_bytes

@dataclass(frozen=True)
class DiskInfo:
    unidade: str
    total_bytes: int
    usados_bytes: int
    livre_bytes: int

    @property
    def used_percent(self) -> float:
        if self.total_bytes == 0:
            return 0.0
        return (self.usados_bytes / self.total_bytes) * 100

    def to_display_lines(self) -> list[str]:
        return [
            f"Unidade analisada: {self.unidade}",
            f"Espaco total: {format_bytes(self.total_bytes)}",
            f"Espaco usado: {format_bytes(self.usados_bytes)}",
            f"Espaco livre: {format_bytes(self.livre_bytes)}",
            f"Uso do disco: {self.used_percent:.2f}%",
        ]