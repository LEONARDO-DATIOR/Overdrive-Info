from machine_monitor.collectors.ProcessorCollector import ProcessorCollector

class ProcessorView:
    
    def show(self):
        Processor = ProcessorCollector().collect()

        print("\n=== Processador ===")
        print(f"Processador: {Processor.processador} | Arquitetura: {Processor.maquina} | Fabricante: {Processor.fabricante}")
        print(f"Cores: {Processor.cores} | Threads: {Processor.threads}")
        print(f"Frequência: {Processor.frequencia} MHz")