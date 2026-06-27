

from machine_monitor.models.SystemModel import SystemInfo


class SystemCollectors:
    def __init__(self):
        pass

    def get_system_info(self):
        import platform
        sistema = SystemInfo(
            sistema_operacional=platform.system(),
            versao=platform.version(),
            hostname=platform.node(),
            usuario_atual=platform.uname().username if hasattr(platform.uname(), 'username') else ""
        )
        return sistema