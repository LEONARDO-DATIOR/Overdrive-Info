from dataclasses import dataclass

@dataclass(frozen=True)
class SystemInfo:
    sistema_operacional: str
    hostname: str
    versao: str
    usuario_atual: str = ""

    def to_display_lines(self) -> list[str]:
        return [
            f"Sistema Operacional: {self.sistema_operacional}",
            f"Hostname: {self.hostname}",
            f"Usuario Atual: {self.usuario_atual}",
            f"Versao: {self.versao}",
        ]