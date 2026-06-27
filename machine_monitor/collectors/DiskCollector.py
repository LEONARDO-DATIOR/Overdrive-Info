from pathlib import Path
import psutil

from machine_monitor.models.DiskModel import DiskInfo

class DiskCollector:
    def collect(self) -> DiskInfo:
        discos = []

        for disco in psutil.disk_partitions(): 
            uso = psutil.disk_usage(disco.mountpoint)

            disco = DiskInfo(
                unidade=disco.device,
                total_bytes=uso.total,
                usados_bytes=uso.used,
                livre_bytes=uso.free,
            );

            discos.append(disco)
        
        return discos

