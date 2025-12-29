#!/usr/bin/env python
"""
SADES - Sistema de Gestión Académica
Punto de entrada de la aplicación
"""

import os
import sys

# Agregar el directorio actual al path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import create_app

app = create_app()

if __name__ == '__main__':
    print("=" * 60)
    print("🚀 SADES - Sistema de Gestión Académica")
    print("=" * 60)
    print()
    print("✅ Aplicación iniciada")
    print()
    print("=" * 60)
    print()
    
    app.run(debug=True)

