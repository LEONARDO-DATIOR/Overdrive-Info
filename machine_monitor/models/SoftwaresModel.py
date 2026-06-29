from dataclasses import dataclass

@dataclass(frozen=True)
class SoftwareInfo:
    nome: str
    versao: str
    fornecedor: str

    def to_display_lines(self) -> list[str]:
        return [
            f"Nome do software: {self.nome}",
            f"Versão: {self.versao}",
            f"Fornecedor: {self.fornecedor}",
        ]