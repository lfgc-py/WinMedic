import ctypes
import psutil
import os

kernel32 = ctypes.windll.kernel32
psapi = ctypes.windll.psapi

def obtener_ram():
    mem = psutil.virtual_memory()
    return {
        "total": mem.total,
        "usada": mem.used,
        "libre": mem.available
    }

def limpiar_working_sets():
    for proc in psutil.process_iter(['pid']):
        try:
            handle = kernel32.OpenProcess(0x1F0FFF, False, proc.info['pid'])
            psapi.EmptyWorkingSet(handle)
            kernel32.CloseHandle(handle)
        except:
            pass

def liberar_ram():
    antes = obtener_ram()["libre"]
    limpiar_working_sets()
    os.system("echo off | powershell.exe Clear-Memory")
    despues = obtener_ram()["libre"]

    liberado = despues - antes
    return f"Memoria liberada: {liberado / (1024**2):.2f} MB"
