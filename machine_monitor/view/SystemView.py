from machine_monitor.collectors.SystemCollectors import SystemCollectors


class SystemView:

    def show(self):
        sistema = SystemCollectors().get_system_info()


        print("\n=== Informacoes do Sistema Operacional ===")
        print(f"Nome do Sistema: {sistema.sistema_operacional}")
        print(f"Versao do Sistema: {sistema.versao}")
        print(f"Nome do Host: {sistema.hostname}")
        print(f"Usuario Atual: {sistema.usuario_atual}")