import winreg

STARTUP_KEYS = [
    (winreg.HKEY_CURRENT_USER,
     r"Software\Microsoft\Windows\CurrentVersion\Run"),
    (winreg.HKEY_LOCAL_MACHINE,
     r"Software\Microsoft\Windows\CurrentVersion\Run")
]

def obtener_programas_inicio():
    programas = []

    for root, path in STARTUP_KEYS:
        try:
            with winreg.OpenKey(root, path) as key:
                for i in range(0, winreg.QueryInfoKey(key)[1]):
                    nombre, valor, _ = winreg.EnumValue(key, i)
                    programas.append((nombre, valor, path))
        except:
            pass

    return programas

def deshabilitar_programa(nombre):
    for root, path in STARTUP_KEYS:
        try:
            with winreg.OpenKey(root, path, 0, winreg.KEY_SET_VALUE) as key:
                winreg.DeleteValue(key, nombre)
                return f"{nombre} deshabilitado del inicio."
        except:
            continue

    return f"No se pudo deshabilitar: {nombre}"
