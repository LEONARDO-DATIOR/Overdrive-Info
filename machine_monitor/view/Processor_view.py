from machine_monitor.collectors.ProcessorCollector import ProcessorCollector

class ProcessorView:
    
    def show(self):
        Processor = ProcessorCollector().collect()

        print("\n=== Processador ===")
        print(f"Processador: {Processor.processador} | Arquitetura: {Processor.maquina}")
        if Processor.total_ram_bytes is not None:
            print(f"Memória RAM Total: {Processor.total_ram_bytes // (1024**3)} GB")
        else:
            print("Memória RAM Total: Não informado")