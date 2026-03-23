from datetime import datetime

def generar_reporte(datos):
    nombre = f"Reporte_WinMedic_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    
    with open(nombre, "w", encoding="utf-8") as archivo:
        archivo.write("===== REPORTE WINMEDIC =====\n\n")
        for k, v in datos.items():
            archivo.write(f"{k}: {v}\n")
        archivo.write("\n===== RECOMENDACIONES =====\n")

        if datos["RAM Usada (%)"] > 80:
            archivo.write("• Uso alto de RAM. Cerrar programas innecesarios.\n")

        if datos["Uso CPU (%)"] > 80:
            archivo.write("• CPU sobrecargado. Revisar procesos.\n")

        archivo.write("\nFin del reporte.\n")

    return nombre
