from dataclasses import dataclass

from machine_monitor.utils.utils import format_bytes

@dataclass(frozen=True)
class ProcessorInfo:
    maquina: str
    processador: str
    fabricante: str | None = None

    frequencia: float | None = None
    cores: int | None = None
    threads: int | None = None

    def to_display_lines(self) -> list[str]:
        return [
            f"Processador: {self.maquina} ",
            f"Processador: {self.processador}",
            f"Fabricante: {self.fabricante}" if self.fabricante else "Fabricante: Não informado",
            f"Cores: {self.cores}",
            f"Threads: {self.threads}",
        ]