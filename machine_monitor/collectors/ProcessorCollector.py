import ctypes
import os
import platform
from cpuinfo import get_cpu_info

from machine_monitor.models.ProcessorModel import ProcessorInfo


class ProcessorCollector:
    def collect(self) -> ProcessorInfo:
        return ProcessorInfo(
            versao=platform.release() or "Nao informado",
            maquina=platform.machine() or "Nao informado",
            processador=get_cpu_info()['brand_raw'] or "Nao informado",
            total_ram_bytes=self._get_total_ram_bytes(),
        )

    def _get_total_ram_bytes(self) -> int | None:
        nome_sistema = platform.system().lower()
        if nome_sistema == "windows":
            return self._get_windows_ram_bytes()

        return self._get_unix_ram_bytes()

    def _get_windows_ram_bytes(self) -> int | None:
        class MemoryStatus(ctypes.Structure):
            _fields_ = [
                ("dwLength", ctypes.c_ulong),
                ("dwMemoryLoad", ctypes.c_ulong),
                ("ullTotalPhys", ctypes.c_ulonglong),
                ("ullAvailPhys", ctypes.c_ulonglong),
                ("ullTotalPageFile", ctypes.c_ulonglong),
                ("ullAvailPageFile", ctypes.c_ulonglong),
                ("ullTotalVirtual", ctypes.c_ulonglong),
                ("ullAvailVirtual", ctypes.c_ulonglong),
                ("ullAvailExtendedVirtual", ctypes.c_ulonglong),
            ]

        status = MemoryStatus()
        status.dwLength = ctypes.sizeof(MemoryStatus)

        if not ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(status)):
            return None

        return int(status.ullTotalPhys)

    def _get_unix_ram_bytes(self) -> int | None:
        try:
            page_size = os.sysconf("SC_PAGE_SIZE")
            physical_pages = os.sysconf("SC_PHYS_PAGES")
        except (AttributeError, ValueError, OSError):
            return None

        return int(page_size * physical_pages)
