from machine_monitor.collectors.DiskCollector import DiskCollector

class DiskView:

    def show(self):

        discos = DiskCollector().collect()
        espaco_total = sum(disco.total_bytes for disco in discos)

        for disco in discos:
            print("\n=== DISCO ===")
            print(f"Unidade: {disco.unidade}")
            print(f"Total: {disco.total_bytes // (1024**3)} GB")
            print(f"Usado: {disco.usados_bytes // (1024**3)} GB")
            print(f"Livre: {disco.livre_bytes // (1024**3)} GB")
        
        print(f"\n=== RESUMO TOTAL ===")
        print(f"Espaço Total: {espaco_total // (1024**3)} GB")
        print(f"Quantidade de Discos: {len(discos)}")