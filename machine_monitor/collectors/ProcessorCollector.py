import platform

import cpuinfo
import psutil

from machine_monitor.models.ProcessorModel import ProcessorInfo


class ProcessorCollector:


    def collect(self) -> ProcessorInfo:
        info = cpuinfo.get_cpu_info()
        
        return ProcessorInfo(
            maquina=platform.machine() or "Nao informado",
            processador=info.get("brand_raw", "Nao informado"),
            fabricante=info.get("vendor_id_raw"),
            cores=psutil.cpu_count(logical=False) or "Nao informado",
            threads=psutil.cpu_count(logical=True) or "Nao informado",
            frequencia=psutil.cpu_freq().current if psutil.cpu_freq() else None
        )