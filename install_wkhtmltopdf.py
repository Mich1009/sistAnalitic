#!/usr/bin/env python
"""
Script para instalar wkhtmltopdf automáticamente
Uso: python install_wkhtmltopdf.py
"""

import os
import sys
import subprocess
import platform

def check_wkhtmltopdf():
    """Verifica si wkhtmltopdf está instalado"""
    try:
        subprocess.run(['wkhtmltopdf', '--version'], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def install_windows():
    """Instala wkhtmltopdf en Windows"""
    print("🪟 Detectado: Windows")
    print()
    print("Opciones de instalación:")
    print("1. Descargar desde: https://wkhtmltopdf.org/downloads.html")
    print("   - Descarga la versión para Windows")
    print("   - Ejecuta el instalador")
    print("   - Marca la opción 'Add wkhtmltopdf to PATH'")
    print()
    print("2. O usa Chocolatey (si está instalado):")
    print("   choco install wkhtmltopdf")
    print()
    print("3. O usa Scoop (si está instalado):")
    print("   scoop install wkhtmltopdf")
    print()

def install_macos():
    """Instala wkhtmltopdf en macOS"""
    print("🍎 Detectado: macOS")
    print()
    print("Instalando wkhtmltopdf con Homebrew...")
    print()
    
    # Verificar si Homebrew está instalado
    try:
        subprocess.run(['brew', '--version'], capture_output=True, check=True)
        print("✅ Homebrew detectado")
        print()
        print("Ejecuta:")
        print("  brew install --cask wkhtmltopdf")
        print()
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Homebrew no está instalado")
        print()
        print("Instala Homebrew primero:")
        print("  /bin/bash -c \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\"")
        print()
        print("Luego instala wkhtmltopdf:")
        print("  brew install --cask wkhtmltopdf")
        print()

def install_linux():
    """Instala wkhtmltopdf en Linux"""
    print("🐧 Detectado: Linux")
    print()
    
    # Detectar distribución
    try:
        with open('/etc/os-release', 'r') as f:
            os_info = f.read().lower()
            
        if 'ubuntu' in os_info or 'debian' in os_info:
            print("📦 Detectado: Debian/Ubuntu")
            print()
            print("Ejecuta:")
            print("  sudo apt-get update")
            print("  sudo apt-get install wkhtmltopdf")
            print()
        elif 'fedora' in os_info or 'rhel' in os_info or 'centos' in os_info:
            print("📦 Detectado: Fedora/RHEL/CentOS")
            print()
            print("Ejecuta:")
            print("  sudo dnf install wkhtmltopdf")
            print()
        elif 'arch' in os_info:
            print("📦 Detectado: Arch Linux")
            print()
            print("Ejecuta:")
            print("  sudo pacman -S wkhtmltopdf")
            print()
        else:
            print("📦 Distribución desconocida")
            print()
            print("Intenta con tu gestor de paquetes:")
            print("  sudo apt-get install wkhtmltopdf  (Debian/Ubuntu)")
            print("  sudo dnf install wkhtmltopdf      (Fedora/RHEL)")
            print("  sudo pacman -S wkhtmltopdf        (Arch)")
            print()
    except FileNotFoundError:
        print("No se pudo detectar la distribución")
        print()
        print("Intenta con tu gestor de paquetes:")
        print("  sudo apt-get install wkhtmltopdf  (Debian/Ubuntu)")
        print("  sudo dnf install wkhtmltopdf      (Fedora/RHEL)")
        print("  sudo pacman -S wkhtmltopdf        (Arch)")
        print()

def main():
    """Función principal"""
    print("=" * 60)
    print("📦 INSTALADOR DE WKHTMLTOPDF")
    print("=" * 60)
    print()
    
    # Verificar si ya está instalado
    print("1️⃣  Verificando si wkhtmltopdf está instalado...")
    if check_wkhtmltopdf():
        print("✅ wkhtmltopdf ya está instalado")
        print()
        print("Verifica la versión:")
        subprocess.run(['wkhtmltopdf', '--version'])
        print()
        return
    
    print("❌ wkhtmltopdf no está instalado")
    print()
    
    # Detectar sistema operativo
    print("2️⃣  Detectando sistema operativo...")
    system = platform.system()
    print()
    
    if system == 'Windows':
        install_windows()
    elif system == 'Darwin':
        install_macos()
    elif system == 'Linux':
        install_linux()
    else:
        print(f"❌ Sistema operativo no soportado: {system}")
        print()
        print("Visita: https://wkhtmltopdf.org/downloads.html")
        print()
        return
    
    print("=" * 60)
    print("📝 DESPUÉS DE INSTALAR")
    print("=" * 60)
    print()
    print("1. Cierra y reabre tu terminal")
    print("2. Verifica la instalación:")
    print("   wkhtmltopdf --version")
    print()
    print("3. Ejecuta tu aplicación:")
    print("   python run.py")
    print()
    print("4. Intenta generar un PDF nuevamente")
    print()

if __name__ == '__main__':
    main()
