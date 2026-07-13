from collections.abc import Callable

# COLLECTORS
from machine_monitor.collectors.DiskCollector import DiskCollector
from machine_monitor.collectors.MemoryCollector import MemoryCollector
from machine_monitor.collectors.ProcessorCollector import ProcessorCollector
from machine_monitor.collectors.SystemCollectors import SystemCollectors
from machine_monitor.collectors.SoftwaresCollectors import SoftwaresCollectors

# VIEWS
from machine_monitor.view.Processor_view import ProcessorView
from machine_monitor.view.Memory_view import MemoryView
from machine_monitor.view.disk_view import DiskView
from machine_monitor.view.SystemView import SystemView
from machine_monitor.view.Softwares_view import SoftwaresView
from machine_monitor.reports.ReportGenerator import ReportGenerator


class InteractiveMenu:
    def __init__(
        self,
        processor_collector: ProcessorCollector | None = None,
        disk_collector: DiskCollector | None = None,
        memory_collector: MemoryCollector | None = None,
        system_collector: SystemView | None = None,
        softwares_collector: SoftwaresCollectors | None = None,
    ) -> None:
        self.processor_collector = processor_collector or ProcessorCollector()
        self.disk_collector = disk_collector or DiskCollector()
        self.memory_collector = memory_collector or MemoryCollector()
        self.system_collector = system_collector or SystemCollectors()
        self.softwares_collector = softwares_collector or SoftwaresCollectors()
        
        self.options: dict[str, Callable[[], bool]] = {
            "1": self.show_processor_info,
            "2": self.show_disk_info,
            "3": self.show_memory_info,
            "4": self.show_system_info,
            "5": self.show_softwares_info,
            "6": self.generate_system_report,
            "7": self.exit_menu,
        }

    def run(self) -> None:
        should_continue = True

        while should_continue:
            self._show_options()
            selected_option = input("Escolha uma opcao: ").strip()
            action = self.options.get(selected_option)

            if action is None:
                print("\nOpcao invalida. Tente novamente.")
                self._wait_for_user()
                continue

            should_continue = action()

    # Action hadware
    def show_processor_info(self) -> bool:
        ProcessorView().show()
        self._wait_for_user()
        return True

    def show_disk_info(self) -> bool:
        DiskView().show()
        self._wait_for_user()
        return True

    def show_memory_info(self) -> bool:
        MemoryView().show()
        self._wait_for_user()
        return True

    # Action system
    def show_system_info(self) -> bool:
        SystemView().show()
        self._wait_for_user()
        return True

    def show_softwares_info(self) -> bool:
        SoftwaresView().show()
        self._wait_for_user()
        return True

    def generate_system_report(self) -> bool:
        print("\nGerando relatorio em HTML...")
        report_path = ReportGenerator().gerar()
        print("\nRelatorio HTML gerado com sucesso!")
        print(f"Arquivo salvo em: {report_path.resolve()}")
        self._wait_for_user()
        return True

    # Extras
    def exit_menu(self) -> bool:
        print("\nEncerrando o monitor. Ate logo!")
        return False

    def _show_section(self, title: str, lines: list[str]) -> None:
        print(f"\n--- {title} ---")
        for line in lines:
            print(line)

    def _wait_for_user(self) -> None:
        input("\nPressione Enter para continuar...")
    
    # Menu opções
    def _show_options(self) -> None:
        print("\n=== Monitor de Especificacoes da Maquina ===")
        print("1 - Exibir do processador")
        print("2 - Exibir do espaco em disco")
        print("3 - Exibir da memoria RAM")
        print("\n=== Monitor de Especificacoes da SO ===")
        print("4 - Exibir informacoes do sistema operacional")
        print("5 - Exibir os softwares instalados")
        print("\n=== Relatorios ===")
        print("6 - Gerar relatorio completo do sistema")
        print("\n7 - Sair")



