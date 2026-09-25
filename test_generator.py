#!/usr/bin/env python3
"""
Script de prueba para validar que el generador de PDF funciona correctamente.
Ejecuta: python test_generator.py
"""

import sys
import os
from pathlib import Path

def test_imports():
    """Prueba que todas las dependencias estén instaladas."""
    print("🔍 Verificando dependencias...")
    
    try:
        import jinja2
        print("  ✓ Jinja2 instalado")
    except ImportError:
        print("  ✗ Jinja2 NO instalado")
        return False
    
    try:
        import weasyprint
        print("  ✓ WeasyPrint instalado")
    except ImportError:
        print("  ✗ WeasyPrint NO instalado")
        return False
    
    return True

def test_file_structure():
    """Verifica que los archivos necesarios existan."""
    print("\n📁 Verificando estructura de archivos...")
    
    required_files = [
        'generar_pdf_correos.py',
        'generar_pdf_desde_json.py',
        'config.py',
        'requirements.txt',
        'README.md',
        'ejemplo_correos.json',
    ]
    
    all_exist = True
    for file in required_files:
        if Path(file).exists():
            print(f"  ✓ {file}")
        else:
            print(f"  ✗ {file} NO ENCONTRADO")
            all_exist = False
    
    return all_exist

def test_json_validity():
    """Verifica que el JSON de ejemplo sea válido."""
    print("\n📋 Verificando validez del JSON...")
    
    import json
    
    try:
        with open('ejemplo_correos.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if isinstance(data, list) and len(data) > 0:
            print(f"  ✓ JSON válido con {len(data)} correos")
            
            # Verificar estructura
            required_keys = ['from', 'subject', 'date', 'body']
            first_email = data[0]
            
            missing_keys = [k for k in required_keys if k not in first_email]
            if missing_keys:
                print(f"  ✗ Faltan campos: {missing_keys}")
                return False
            
            print(f"  ✓ Estructura de correos válida")
            return True
        else:
            print("  ✗ JSON no es una lista o está vacío")
            return False
    
    except json.JSONDecodeError as e:
        print(f"  ✗ JSON inválido: {e}")
        return False
    except FileNotFoundError:
        print("  ✗ Archivo ejemplo_correos.json no encontrado")
        return False

def test_pdf_generation():
    """Prueba la generación de un PDF simple."""
    print("\n🔨 Probando generación de PDF...")
    
    try:
        from generar_pdf_desde_json import generate_pdf_from_json
        
        # Usar el archivo de ejemplo
        output_file = 'test_output.pdf'
        
        print(f"  Generando PDF de prueba: {output_file}")
        success = generate_pdf_from_json('ejemplo_correos.json', output_file)
        
        if success and Path(output_file).exists():
            file_size = Path(output_file).stat().st_size
            print(f"  ✓ PDF generado exitosamente ({file_size} bytes)")
            
            # Limpiar archivo de prueba
            os.remove(output_file)
            print(f"  ✓ Archivo de prueba eliminado")
            
            return True
        else:
            print("  ✗ Error al generar PDF")
            return False
    
    except Exception as e:
        print(f"  ✗ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_config():
    """Verifica que el archivo de configuración sea válido."""
    print("\n⚙️  Verificando configuración...")
    
    try:
        import config
        
        # Verificar que existan las claves principales
        required_keys = ['COLORS', 'FONTS', 'MARGINS', 'PAGE', 'DOCUMENT']
        
        for key in required_keys:
            if hasattr(config, key):
                print(f"  ✓ {key} definido")
            else:
                print(f"  ✗ {key} NO definido")
                return False
        
        return True
    
    except ImportError as e:
        print(f"  ✗ Error al importar config: {e}")
        return False

def run_all_tests():
    """Ejecuta todas las pruebas."""
    print("=" * 70)
    print("🧪 PRUEBAS DEL GENERADOR DE PDF DE CORREOS")
    print("=" * 70)
    
    results = {
        'Dependencias': test_imports(),
        'Estructura de archivos': test_file_structure(),
        'Validez del JSON': test_json_validity(),
        'Configuración': test_config(),
        'Generación de PDF': test_pdf_generation(),
    }
    
    print("\n" + "=" * 70)
    print("📊 RESUMEN DE PRUEBAS")
    print("=" * 70)
    
    passed = sum(1 for v in results.values() if v)
    total = len(results)
    
    for test_name, result in results.items():
        status = "✓ PASÓ" if result else "✗ FALLÓ"
        print(f"{test_name:.<50} {status}")
    
    print("=" * 70)
    print(f"Resultado: {passed}/{total} pruebas pasadas")
    print("=" * 70)
    
    if passed == total:
        print("\n✅ ¡TODAS LAS PRUEBAS PASARON!")
        print("\nPuedes usar el generador con:")
        print("  python generar_pdf_correos.py")
        print("  python generar_pdf_desde_json.py ejemplo_correos.json")
        return 0
    else:
        print("\n❌ ALGUNAS PRUEBAS FALLARON")
        print("\nPor favor, verifica:")
        print("  1. Que todas las dependencias estén instaladas: pip install -r requirements.txt")
        print("  2. Que todos los archivos estén presentes")
        print("  3. Que el JSON sea válido")
        return 1

if __name__ == "__main__":
    exit_code = run_all_tests()
    sys.exit(exit_code)
