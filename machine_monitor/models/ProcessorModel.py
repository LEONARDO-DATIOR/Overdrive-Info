from dataclasses import dataclass

from machine_monitor.utils.utils import format_bytes

@dataclass(frozen=True)
class ProcessorInfo:
    versao: str
    maquina: str
    processador: str
    total_ram_bytes: int | None

    def to_display_lines(self) -> list[str]:
        return [
            f"Processador: {self.maquina} ",
            f"Processador: {self.processador}",
            f"Memoria RAM total: {format_bytes(self.total_ram_bytes)}",
        ]