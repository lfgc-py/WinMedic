import tkinter as tk
from system_info import get_system_info
from maintenance import limpiar_temporales, vaciar_papelera, ejecutar_sfc, ejecutar_chkdsk
from report import generar_reporte
from maintenance import ejecutar_dism
from maintenance import limpiar_dns, restaurar_red, escanear_defender, limpiar_windows_update
import ctypes
import sys
from startup_manager import obtener_programas_inicio, deshabilitar_programa
from ram_manager import liberar_ram


def es_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not es_admin():
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, __file__, None, 1
    )
    sys.exit()


COLOR_FONDO = "#1e1e1e"
COLOR_TEXTO = "#e0e0e0"
COLOR_BOTON = "#2d89ef"
COLOR_BOTON_TEXTO = "#ffffff"
COLOR_AREA = "#252526"

def crear_reporte():
    datos = get_system_info()
    archivo = generar_reporte(datos)
    area_texto.insert(tk.END, f"\nReporte generado: {archivo}\n")

def mostrar_diagnostico():
    area_texto.delete(1.0, tk.END)
    data = get_system_info()
    for k, v in data.items():
        area_texto.insert(tk.END, f"{k}: {v}\n")

def ejecutar_accion(funcion):
    resultado = funcion()
    area_texto.insert(tk.END, f"\n{resultado}\n")

def mostrar_inicio():
    area_texto.delete(1.0, tk.END)
    programas = obtener_programas_inicio()

    for i, (nombre, ruta, _) in enumerate(programas):
        area_texto.insert(tk.END, f"{i+1}. {nombre}\n    {ruta}\n\n")

def eliminar_inicio():
    seleccion = area_texto.get("sel.first", "sel.last").strip()
    if not seleccion:
        area_texto.insert(tk.END, "\nSelecciona el nombre del programa primero.\n")
        return

    resultado = deshabilitar_programa(seleccion)
    area_texto.insert(tk.END, f"\n{resultado}\n")


ventana = tk.Tk()
ventana.configure(bg=COLOR_FONDO)
ventana.title("WinMedic")
ventana.geometry("600x500")

frame_botones = tk.Frame(ventana, bg=COLOR_FONDO)
frame_botones.pack(pady=10)

tk.Button(frame_botones, 
    text="Diagnóstico", width=20,  bg=COLOR_BOTON,
    fg=COLOR_BOTON_TEXTO,
    activebackground="#1b5fa7",
    activeforeground="#ffffff", 
    command=mostrar_diagnostico).grid(row=0, column=0, padx=5)

tk.Button(frame_botones, 
    text="Limpiar Temporales", width=20, bg=COLOR_BOTON,
    fg=COLOR_BOTON_TEXTO,
    activebackground="#1b5fa7",
    activeforeground="#ffffff", 
    command=lambda: ejecutar_accion(limpiar_temporales)).grid(row=0, column=1, padx=5)

tk.Button(frame_botones, text="Vaciar Papelera", width=20,  bg=COLOR_BOTON,
    fg=COLOR_BOTON_TEXTO,
    activebackground="#1b5fa7",
    activeforeground="#ffffff",
    command=lambda: ejecutar_accion(vaciar_papelera)).grid(row=1, column=0, padx=5)

tk.Button(frame_botones, text="SFC /scannow", width=20, bg=COLOR_BOTON,
    fg=COLOR_BOTON_TEXTO,
    activebackground="#1b5fa7",
    activeforeground="#ffffff", 
    command=lambda: ejecutar_accion(ejecutar_sfc)).grid(row=1, column=1, padx=5)

tk.Button(frame_botones, text="CHKDSK", width=20, bg=COLOR_BOTON,
    fg=COLOR_BOTON_TEXTO,
    activebackground="#1b5fa7",
    activeforeground="#ffffff", 
    command=lambda: ejecutar_accion(ejecutar_chkdsk)).grid(row=2, column=0, padx=5)

tk.Button(frame_botones, text="Generar Reporte", width=20, bg=COLOR_BOTON,
    fg=COLOR_BOTON_TEXTO,
    activebackground="#1b5fa7",
    activeforeground="#ffffff", 
    command=crear_reporte).grid(row=2, column=1, padx=5)

tk.Button(
    frame_botones,
    text="DISM Repair",
    width=20,
    bg="#ef2d2d",
    fg=COLOR_BOTON_TEXTO,
    activebackground="#8c1515",
    activeforeground="#ffffff",
    command=lambda: ejecutar_accion(ejecutar_dism)
).grid(row=3, column=0, padx=5, pady=5)

tk.Button(frame_botones, text="Limpiar DNS", width=20,
          bg=COLOR_BOTON, fg=COLOR_BOTON_TEXTO,
          command=lambda: ejecutar_accion(limpiar_dns)).grid(row=3, column=1, padx=5, pady=5)

tk.Button(frame_botones, text="Restaurar Red", width=20,
          bg=COLOR_BOTON, fg=COLOR_BOTON_TEXTO,
          command=lambda: ejecutar_accion(restaurar_red)).grid(row=4, column=0, padx=5, pady=5)

tk.Button(frame_botones, text="Defender Scan", width=20,
          bg=COLOR_BOTON, fg=COLOR_BOTON_TEXTO,
          command=lambda: ejecutar_accion(escanear_defender)).grid(row=4, column=1, padx=5, pady=5)

tk.Button(frame_botones, text="Fix Windows Update", width=20,
          bg=COLOR_BOTON, fg=COLOR_BOTON_TEXTO,
          command=lambda: ejecutar_accion(limpiar_windows_update)).grid(row=5, column=0, padx=5, pady=5)


tk.Button(frame_botones, text="Ver Inicio", width=20,
          bg=COLOR_BOTON, fg=COLOR_BOTON_TEXTO,
          command=mostrar_inicio).grid(row=6, column=0, padx=5, pady=5)

tk.Button(frame_botones, text="Deshabilitar Inicio", width=20,
          bg="#c0392b", fg=COLOR_BOTON_TEXTO,
          command=eliminar_inicio).grid(row=6, column=1, padx=5, pady=5)

tk.Button(frame_botones, text="Liberar RAM", width=20,
          bg="#44c767", fg="white",
          command=lambda: ejecutar_accion(liberar_ram)
).grid(row=5, column=1, padx=5, pady=5)


area_texto = tk.Text(ventana)
area_texto.pack(expand=True, fill="both", padx=10, pady=10)

ventana.mainloop()
