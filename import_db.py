#!/usr/bin/env python
"""
Script para importar la base de datos a PostgreSQL
Uso: python import_db.py
"""

import os
import sys
import subprocess
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Obtener credenciales de PostgreSQL
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'postgres')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '5432')
DB_NAME = os.getenv('DB_NAME', 'sades_db')

# Archivo SQL a importar
SQL_FILE = 'grupo1_postgres.sql'

def check_postgres_installed():
    """Verifica si PostgreSQL está instalado"""
    try:
        subprocess.run(['psql', '--version'], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def check_postgres_running():
    """Verifica si PostgreSQL está corriendo"""
    try:
        subprocess.run(
            ['psql', '-U', DB_USER, '-h', DB_HOST, '-p', DB_PORT, '-c', 'SELECT 1'],
            capture_output=True,
            check=True,
            env={**os.environ, 'PGPASSWORD': DB_PASSWORD}
        )
        return True
    except subprocess.CalledProcessError:
        return False

def database_exists():
    """Verifica si la base de datos ya existe"""
    try:
        result = subprocess.run(
            ['psql', '-U', DB_USER, '-h', DB_HOST, '-p', DB_PORT, '-lqt'],
            capture_output=True,
            text=True,
            env={**os.environ, 'PGPASSWORD': DB_PASSWORD}
        )
        databases = [line.split('|')[0].strip() for line in result.stdout.split('\n')]
        return DB_NAME in databases
    except subprocess.CalledProcessError:
        return False

def create_database():
    """Crea la base de datos"""
    print(f"📦 Creando base de datos '{DB_NAME}'...")
    try:
        # Intenta primero con UTF8 y collation en_US
        subprocess.run(
            [
                'psql', '-U', DB_USER, '-h', DB_HOST, '-p', DB_PORT,
                '-c', f'CREATE DATABASE {DB_NAME} WITH ENCODING "UTF8" LC_COLLATE "en_US.UTF-8" LC_CTYPE "en_US.UTF-8" TEMPLATE template0;'
            ],
            capture_output=True,
            check=True,
            env={**os.environ, 'PGPASSWORD': DB_PASSWORD}
        )
        print(f"✅ Base de datos '{DB_NAME}' creada exitosamente")
        return True
    except subprocess.CalledProcessError as e:
        error_msg = e.stderr.decode()
        print(f"⚠️  Intentando con collation del sistema...")
        try:
            # Si falla, intenta con collation del sistema
            subprocess.run(
                [
                    'psql', '-U', DB_USER, '-h', DB_HOST, '-p', DB_PORT,
                    '-c', f'CREATE DATABASE {DB_NAME} WITH ENCODING "UTF8" TEMPLATE template0;'
                ],
                capture_output=True,
                check=True,
                env={**os.environ, 'PGPASSWORD': DB_PASSWORD}
            )
            print(f"✅ Base de datos '{DB_NAME}' creada exitosamente (con collation del sistema)")
            return True
        except subprocess.CalledProcessError as e2:
            print(f"❌ Error al crear la base de datos: {e2.stderr.decode()}")
            return False

def import_sql_file():
    """Importa el archivo SQL a la base de datos"""
    if not os.path.exists(SQL_FILE):
        print(f"❌ Error: El archivo '{SQL_FILE}' no existe")
        return False
    
    print(f"📥 Importando datos desde '{SQL_FILE}'...")
    try:
        with open(SQL_FILE, 'r', encoding='utf-8') as f:
            sql_content = f.read()
        
        process = subprocess.Popen(
            ['psql', '-U', DB_USER, '-h', DB_HOST, '-p', DB_PORT, '-d', DB_NAME],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env={**os.environ, 'PGPASSWORD': DB_PASSWORD}
        )
        
        stdout, stderr = process.communicate(input=sql_content.encode('utf-8'))
        
        if process.returncode != 0:
            print(f"❌ Error al importar datos: {stderr.decode()}")
            return False
        
        print(f"✅ Datos importados exitosamente")
        return True
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

def verify_import():
    """Verifica que la importación fue exitosa"""
    print("🔍 Verificando importación...")
    try:
        result = subprocess.run(
            ['psql', '-U', DB_USER, '-h', DB_HOST, '-p', DB_PORT, '-d', DB_NAME, '-c', '\\dt'],
            capture_output=True,
            text=True,
            env={**os.environ, 'PGPASSWORD': DB_PASSWORD}
        )
        
        # Contar tablas
        lines = result.stdout.strip().split('\n')
        table_count = len([l for l in lines if '|' in l and 'public' in l])
        
        if table_count > 0:
            print(f"✅ Verificación exitosa: {table_count} tablas encontradas")
            print("\n📊 Tablas importadas:")
            print(result.stdout)
            return True
        else:
            print("❌ No se encontraron tablas")
            return False
    except subprocess.CalledProcessError as e:
        print(f"❌ Error en verificación: {e.stderr.decode()}")
        return False

def main():
    """Función principal"""
    print("=" * 60)
    print("🚀 IMPORTADOR DE BASE DE DATOS SADES - PostgreSQL")
    print("=" * 60)
    print()
    
    # Verificar PostgreSQL instalado
    print("1️⃣  Verificando PostgreSQL...")
    if not check_postgres_installed():
        print("❌ PostgreSQL no está instalado o no está en el PATH")
        print("   Descárgalo desde: https://www.postgresql.org/download/")
        sys.exit(1)
    print("✅ PostgreSQL está instalado")
    print()
    
    # Verificar PostgreSQL corriendo
    print("2️⃣  Verificando conexión a PostgreSQL...")
    print(f"   Host: {DB_HOST}:{DB_PORT}")
    print(f"   Usuario: {DB_USER}")
    if not check_postgres_running():
        print("❌ No se puede conectar a PostgreSQL")
        print("   Asegúrate de que PostgreSQL esté corriendo")
        print("   Verifica las credenciales en .env")
        sys.exit(1)
    print("✅ Conexión exitosa")
    print()
    
    # Verificar archivo SQL
    print("3️⃣  Verificando archivo SQL...")
    if not os.path.exists(SQL_FILE):
        print(f"❌ El archivo '{SQL_FILE}' no existe")
        sys.exit(1)
    print(f"✅ Archivo '{SQL_FILE}' encontrado")
    print()
    
    # Crear o usar base de datos existente
    print("4️⃣  Preparando base de datos...")
    if database_exists():
        print(f"⚠️  La base de datos '{DB_NAME}' ya existe")
        response = input("   ¿Deseas eliminarla y crear una nueva? (s/n): ").lower()
        if response == 's':
            print(f"   Eliminando base de datos '{DB_NAME}'...")
            try:
                subprocess.run(
                    ['psql', '-U', DB_USER, '-h', DB_HOST, '-p', DB_PORT, '-c', f'DROP DATABASE IF EXISTS {DB_NAME};'],
                    capture_output=True,
                    check=True,
                    env={**os.environ, 'PGPASSWORD': DB_PASSWORD}
                )
                print(f"   ✅ Base de datos eliminada")
                if not create_database():
                    sys.exit(1)
            except subprocess.CalledProcessError as e:
                print(f"   ❌ Error: {e.stderr.decode()}")
                sys.exit(1)
        else:
            print("   Usando base de datos existente")
    else:
        if not create_database():
            sys.exit(1)
    print()
    
    # Importar datos
    print("5️⃣  Importando datos...")
    if not import_sql_file():
        sys.exit(1)
    print()
    
    # Verificar importación
    print("6️⃣  Verificando importación...")
    if not verify_import():
        sys.exit(1)
    print()
    
    print("=" * 60)
    print("✅ ¡IMPORTACIÓN COMPLETADA EXITOSAMENTE!")
    print("=" * 60)
    print()
    print("📝 Próximos pasos:")
    print("   1. Activa el entorno virtual:")
    print("      venv\\Scripts\\activate  (Windows)")
    print("      source venv/bin/activate  (macOS/Linux)")
    print()
    print("   2. Instala las dependencias:")
    print("      pip install -r requirements.txt")
    print()
    print("   3. Ejecuta la aplicación:")
    print("      python run.py")
    print()
    print("🔐 Usuarios de prueba:")
    print("   Admin: admin / admin123")
    print("   Coordinador: coordinador / coord123")
    print("   Docente: docente / docente123")
    print()

if __name__ == '__main__':
    main()
