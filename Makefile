.PHONY: help install test run run-json clean docs

# Variables
PYTHON := python3
PIP := pip3
VENV := venv

help:
	@echo "📧 Email to PDF Generator - Comandos disponibles"
	@echo "=================================================="
	@echo ""
	@echo "Instalación:"
	@echo "  make install          - Instalar dependencias"
	@echo "  make venv             - Crear entorno virtual"
	@echo ""
	@echo "Ejecución:"
	@echo "  make run              - Generar PDF con datos de ejemplo"
	@echo "  make run-json         - Generar PDF desde JSON"
	@echo "  make test             - Ejecutar pruebas"
	@echo ""
	@echo "Limpieza:"
	@echo "  make clean            - Limpiar archivos generados"
	@echo "  make clean-all        - Limpiar todo incluyendo venv"
	@echo ""
	@echo "Documentación:"
	@echo "  make docs             - Mostrar documentación"
	@echo ""

install:
	@echo "📦 Instalando dependencias..."
	$(PIP) install -r requirements.txt
	@echo "✅ Dependencias instaladas"

venv:
	@echo "🔧 Creando entorno virtual..."
	$(PYTHON) -m venv $(VENV)
	@echo "✅ Entorno virtual creado"
	@echo "Actívalo con: source $(VENV)/bin/activate"

test:
	@echo "🧪 Ejecutando pruebas..."
	$(PYTHON) test_generator.py

run:
	@echo "🚀 Generando PDF con datos de ejemplo..."
	$(PYTHON) generar_pdf_correos.py
	@echo "✅ PDF generado: correos_gmail.pdf"

run-json:
	@echo "🚀 Generando PDF desde JSON..."
	$(PYTHON) generar_pdf_desde_json.py ejemplo_correos.json
	@echo "✅ PDF generado: correos_gmail.pdf"

run-json-custom:
	@echo "🚀 Generando PDF desde JSON personalizado..."
	@read -p "Ingresa el archivo JSON: " json_file; \
	read -p "Ingresa el nombre del PDF (default: correos_gmail.pdf): " pdf_file; \
	if [ -z "$$pdf_file" ]; then pdf_file="correos_gmail.pdf"; fi; \
	$(PYTHON) generar_pdf_desde_json.py $$json_file -o $$pdf_file

clean:
	@echo "🧹 Limpiando archivos generados..."
	rm -f correos_gmail.pdf test_output.pdf
	rm -f temp.json temp_emails.json
	rm -f debug_output.html
	rm -rf __pycache__ .cache
	rm -f *.pyc
	rm -f pdf_generator.log
	@echo "✅ Limpieza completada"

clean-all: clean
	@echo "🧹 Limpiando todo incluyendo entorno virtual..."
	rm -rf $(VENV)
	@echo "✅ Limpieza total completada"

docs:
	@echo "📚 Documentación disponible:"
	@echo ""
	@echo "1. README.md - Documentación completa"
	@echo "   Contiene: instalación, uso, características, solución de problemas"
	@echo ""
	@echo "2. QUICKSTART.md - Guía de inicio rápido"
	@echo "   Contiene: pasos simples para empezar en 5 minutos"
	@echo ""
	@echo "3. GUIA_AVANZADA.md - Guía avanzada"
	@echo "   Contiene: personalización, integración con APIs, optimización"
	@echo ""
	@echo "4. PROYECTO_RESUMEN.md - Resumen del proyecto"
	@echo "   Contiene: objetivos, características, estadísticas"
	@echo ""
	@echo "Abre cualquiera de estos archivos para más información."

# Comandos adicionales útiles
check-deps:
	@echo "🔍 Verificando dependencias..."
	$(PYTHON) -c "import jinja2; print('✓ Jinja2 instalado')" || echo "✗ Jinja2 NO instalado"
	$(PYTHON) -c "import weasyprint; print('✓ WeasyPrint instalado')" || echo "✗ WeasyPrint NO instalado"

validate-json:
	@echo "📋 Validando JSON..."
	$(PYTHON) -m json.tool ejemplo_correos.json > /dev/null && echo "✅ JSON válido" || echo "❌ JSON inválido"

format:
	@echo "🎨 Formateando código..."
	$(PYTHON) -m black generar_pdf_correos.py generar_pdf_desde_json.py config.py test_generator.py 2>/dev/null || echo "⚠️  black no instalado (opcional)"

lint:
	@echo "🔍 Analizando código..."
	$(PYTHON) -m pylint generar_pdf_correos.py 2>/dev/null || echo "⚠️  pylint no instalado (opcional)"

# Alias útiles
setup: venv install
	@echo "✅ Configuración completada"

quick: test run
	@echo "✅ Pruebas y generación completadas"

all: clean install test run
	@echo "✅ Proceso completo finalizado"

.DEFAULT_GOAL := help
