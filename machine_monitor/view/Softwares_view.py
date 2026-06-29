from machine_monitor.collectors.SoftwaresCollectors import SoftwaresCollectors



class SoftwaresView:
        
    def show(self) -> None:
        IGNORAR = [
            "Microsoft windows Desktop",        
            "Microsoft Visual C++",
            "NVIDIA",
            "Microsoft .NET",
        ]
        softwares = SoftwaresCollectors().collect()
        
        print("\n=== SOFTWARE ===")
        for software in softwares:

            if any(ignorar.lower() in software.nome.lower() for ignorar in IGNORAR):
                continue

            print(f"\n\nNome: {software.nome}")
            print(f"Versão: {software.versao}")
            print(f"Fornecedor: {software.fornecedor}")
