import os
import subprocess
import shutil

def limpiar_temporales():
    temp_path = os.environ.get("TEMP")
    try:
        shutil.rmtree(temp_path, ignore_errors=True)
        os.makedirs(temp_path, exist_ok=True)
        return "Archivos temporales eliminados"
    except:
        return "Error al limpiar temporales"

def vaciar_papelera():
    try:
        subprocess.run("PowerShell.exe -Command Clear-RecycleBin -Force", shell=True)
        return "Papelera vaciada"
    except:
        return "Error al vaciar papelera"

def ejecutar_sfc():
    subprocess.Popen("sfc /scannow", shell=True)
    return "Comprobador de archivos iniciado"

def ejecutar_chkdsk():
    proceso = subprocess.Popen(
        "chkdsk",
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    salida, error = proceso.communicate()

    if salida:
        return salida
    if error:
        return error
    return "CHKDSK finalizado sin mensajes."


def abrir_administrador_dispositivos():
    subprocess.Popen("devmgmt.msc", shell=True)

def ejecutar_dism():
    subprocess.Popen("DISM /Online /Cleanup-Image /RestoreHealth", shell=True)
    return "DISM iniciado (reparación profunda de Windows)"

def limpiar_dns():
    subprocess.Popen("ipconfig /flushdns", shell=True)
    return "Caché DNS limpiada"

def restaurar_red():
    subprocess.Popen("netsh int ip reset", shell=True)
    return "Red restaurada"


def escanear_defender():
    defender_path = os.path.join(
        os.environ.get("ProgramFiles", "C:\\Program Files"),
        "Windows Defender",
        "MpCmdRun.exe"
    )

    comando = f'"{defender_path}" -Scan -ScanType 1'
    subprocess.Popen(comando, shell=True)

    return "Escaneo rápido de Windows Defender iniciado"

def limpiar_windows_update():
    subprocess.Popen("net stop wuauserv && net stop bits && del /s /q C:\Windows\SoftwareDistribution\* && net start wuauserv && net start bits", shell=True)
    return "Componentes de Windows Update limpiados"



