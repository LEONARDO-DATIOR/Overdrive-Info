import wmi

from machine_monitor.models.MemoryModel import MemoryInfo

c = wmi.WMI()

class MemoryCollector:
    def collect(self) -> MemoryInfo:
        memorias = []

        for memoria in c.Win32_PhysicalMemory():
            memoria = MemoryInfo(
                fabricant=memoria.Manufacturer,
                capacidade=int(memoria.Capacity),
                velocidade=int(memoria.Speed),
                part_number=memoria.PartNumber,
            )

            memorias.append(memoria)

        return memorias
         