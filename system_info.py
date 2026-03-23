import psutil
import platform
from datetime import datetime

def get_system_info():
    info = {}

    info["Fecha"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    info["Sistema"] = platform.system()
    info["Versión"] = platform.version()
    info["Arquitectura"] = platform.machine()
    info["Procesador"] = platform.processor()

    # CPU
    info["Uso CPU (%)"] = psutil.cpu_percent(interval=1)

    # RAM
    mem = psutil.virtual_memory()
    info["RAM Total (GB)"] = round(mem.total / (1024**3), 2)
    info["RAM Usada (%)"] = mem.percent

    # Disco
    disk = psutil.disk_usage("/")
    info["Disco Total (GB)"] = round(disk.total / (1024**3), 2)
    info["Disco Libre (GB)"] = round(disk.free / (1024**3), 2)

    # Batería (si existe)
    battery = psutil.sensors_battery()
    if battery:
        info["Batería (%)"] = battery.percent
        info["Conectado"] = battery.power_plugged
    else:
        info["Batería"] = "No detectada"

    # Tiempo encendido
    uptime_seconds = int(datetime.now().timestamp() - psutil.boot_time())
    hours = uptime_seconds // 3600
    minutes = (uptime_seconds % 3600) // 60
    info["Tiempo encendido"] = f"{hours}h {minutes}m"

    return info
