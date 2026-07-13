import winreg
from machine_monitor.models.SoftwaresModel import SoftwareInfo



class SoftwaresCollectors:

    def collect(self) -> list[SoftwareInfo]:
        CHAVES = [
            (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"),

            (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"),

            (winreg.HKEY_CURRENT_USER, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"),
        ]
        softwares = []

        for hkey, subkey in CHAVES:
            
            with winreg.OpenKey(hkey, subkey) as key:
                for i in range(winreg.QueryInfoKey(key)[0]):
                    subkey_name = winreg.EnumKey(key, i)


                    with winreg.OpenKey(key, subkey_name) as subkey:
                        try:
                            nome = winreg.QueryValueEx(subkey, "DisplayName")[0]
                            if "Microsoft Visual C++" in nome:
                                continue
                            
                            versao = winreg.QueryValueEx(subkey, "DisplayVersion")[0]
                            fornecedor = winreg.QueryValueEx(subkey, "Publisher")[0]

                            software_info = SoftwareInfo(
                                nome=nome[:15],
                                versao=versao,
                                fornecedor=fornecedor
                            )

                            softwares.append(software_info)
                        except FileNotFoundError:
                            pass
        
        return softwares
    