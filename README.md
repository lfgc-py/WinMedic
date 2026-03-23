# 🧬 WinMedic  
### Windows Maintenance & Recovery Toolkit

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-Free-green)

---

## 🧠 Descripción

**WinMedic** es una herramienta de diagnóstico, optimización y reparación del sistema operativo Windows, diseñada para centralizar múltiples utilidades críticas en una sola interfaz gráfica.

Está pensada para usuarios técnicos, entusiastas y profesionales que buscan ejecutar tareas de mantenimiento de forma rápida, estructurada y controlada.

---

## ⚙️ Capacidades principales

WinMedic integra múltiples capas de mantenimiento:

### 🔍 Diagnóstico
- Información completa del sistema
- Estado general del entorno

### 🧹 Limpieza
- Eliminación de archivos temporales
- Vaciado de papelera

### 🛠️ Reparación del sistema
- SFC (`sfc /scannow`)
- CHKDSK
- DISM (reparación profunda de imagen)

### 🌐 Red
- Flush DNS
- Restauración completa de red

### 🛡️ Seguridad
- Escaneo con Windows Defender

### 🔄 Actualizaciones
- Reparación de Windows Update

### ⚡ Optimización
- Liberación de memoria RAM

### 🚀 Control de inicio
- Visualización de programas de arranque
- Deshabilitación selectiva

### 📄 Reportes
- Generación de reportes del sistema

---

## 🧩 Arquitectura del proyecto

```bash
winmedic/
│
├── main.py                # Interfaz gráfica (Tkinter)
├── system_info.py        # Recolección de información del sistema
├── maintenance.py        # Funciones de mantenimiento y reparación
├── report.py             # Generación de reportes
├── startup_manager.py    # Gestión de programas de inicio
├── ram_manager.py        # Optimización de memoria RAM
└── README.md