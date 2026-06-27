
from machine_monitor.collectors.MemoryCollector import MemoryCollector


class MemoryView:
    
    def show(self):
        memorias = MemoryCollector().collect()
        capacidade_total = sum(memoria.capacidade for memoria in memorias)


        for memoria in memorias:
            print("\n=== MEMÓRIA ===")
            print(f"Fabricante: {memoria.fabricant}")
            print(f"Capacidade: {memoria.capacidade // (1024**3)} GB")
            print(f"Velocidade: {memoria.velocidade} MHz")

        print(f"\n=== RESUMO TOTAL ===")
        print(f"Capacidade Total: {capacidade_total // (1024**3)} GB")
        print(f"Quantidade de Memórias: {len(memorias)}")