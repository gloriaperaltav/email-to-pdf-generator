#!/bin/bash

# Script de instalación automática para Email to PDF Generator
# Uso: bash setup.sh

set -e  # Salir si hay error

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Funciones
print_header() {
    echo -e "${BLUE}════════════════════════════════════════════════════════════${NC}"
    echo -e "${BLUE}$1${NC}"
    echo -e "${BLUE}════════════════════════════════════════════════════════════${NC}"
}

print_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

print_error() {
    echo -e "${RED}✗ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠ $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ $1${NC}"
}

# Inicio
print_header "📧 Email to PDF Generator - Instalación Automática"

# Verificar Python
print_info "Verificando Python..."
if ! command -v python3 &> /dev/null; then
    print_error "Python 3 no está instalado"
    echo "Por favor, instala Python 3 desde https://www.python.org/"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
print_success "Python $PYTHON_VERSION encontrado"

# Verificar pip
print_info "Verificando pip..."
if ! command -v pip3 &> /dev/null; then
    print_error "pip3 no está instalado"
    exit 1
fi

print_success "pip3 encontrado"

# Detectar sistema operativo
print_info "Detectando sistema operativo..."
OS_TYPE=$(uname -s)

if [[ "$OS_TYPE" == "Darwin" ]]; then
    print_info "Sistema: macOS"
    
    # Verificar Homebrew
    if ! command -v brew &> /dev/null; then
        print_warning "Homebrew no está instalado"
        echo "Se recomienda instalar Homebrew para las dependencias del sistema"
        echo "Visita: https://brew.sh/"
    else
        print_info "Instalando dependencias del sistema con Homebrew..."
        brew install cairo pango gdk-pixbuf libffi 2>/dev/null || print_warning "Algunas dependencias ya están instaladas"
        print_success "Dependencias del sistema instaladas"
    fi
    
elif [[ "$OS_TYPE" == "Linux" ]]; then
    print_info "Sistema: Linux"
    
    # Detectar distribución
    if [ -f /etc/os-release ]; then
        . /etc/os-release
        DISTRO=$ID
        
        if [[ "$DISTRO" == "ubuntu" ]] || [[ "$DISTRO" == "debian" ]]; then
            print_info "Instalando dependencias del sistema con apt..."
            sudo apt-get update
            sudo apt-get install -y python3-dev libcairo2-dev libpango-1.0-0 libpango-cairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev 2>/dev/null || print_warning "Algunas dependencias ya están instaladas"
            print_success "Dependencias del sistema instaladas"
        fi
    fi
    
elif [[ "$OS_TYPE" == "MINGW64_NT" ]] || [[ "$OS_TYPE" == "MSYS_NT" ]]; then
    print_info "Sistema: Windows"
    print_warning "En Windows, algunas dependencias pueden requerir instalación manual"
    echo "Consulta: https://weasyprint.org/install/"
fi

# Crear entorno virtual (opcional)
print_info "¿Deseas crear un entorno virtual? (recomendado) [s/n]"
read -r CREATE_VENV

if [[ "$CREATE_VENV" == "s" ]] || [[ "$CREATE_VENV" == "S" ]]; then
    print_info "Creando entorno virtual..."
    python3 -m venv venv
    print_success "Entorno virtual creado"
    
    # Activar entorno virtual
    if [[ "$OS_TYPE" == "MINGW64_NT" ]] || [[ "$OS_TYPE" == "MSYS_NT" ]]; then
        source venv/Scripts/activate
    else
        source venv/bin/activate
    fi
    print_success "Entorno virtual activado"
fi

# Instalar dependencias Python
print_info "Instalando dependencias Python..."
pip3 install -r requirements.txt
print_success "Dependencias Python instaladas"

# Ejecutar pruebas
print_info "¿Deseas ejecutar las pruebas? [s/n]"
read -r RUN_TESTS

if [[ "$RUN_TESTS" == "s" ]] || [[ "$RUN_TESTS" == "S" ]]; then
    print_info "Ejecutando pruebas..."
    python3 test_generator.py
fi

# Generar PDF de ejemplo
print_info "¿Deseas generar un PDF de ejemplo? [s/n]"
read -r GENERATE_PDF

if [[ "$GENERATE_PDF" == "s" ]] || [[ "$GENERATE_PDF" == "S" ]]; then
    print_info "Generando PDF de ejemplo..."
    python3 generar_pdf_correos.py
fi

# Resumen final
print_header "✅ Instalación Completada"

echo ""
echo "📚 Próximos pasos:"
echo ""
echo "1. Lee la documentación:"
echo "   - README.md (documentación completa)"
echo "   - QUICKSTART.md (inicio rápido)"
echo "   - GUIA_AVANZADA.md (temas avanzados)"
echo ""
echo "2. Genera tu primer PDF:"
echo "   python3 generar_pdf_correos.py"
echo ""
echo "3. Personaliza los estilos:"
echo "   Edita config.py"
echo ""
echo "4. Usa tus propios correos:"
echo "   python3 generar_pdf_desde_json.py tu_archivo.json"
echo ""

if [[ "$CREATE_VENV" == "s" ]] || [[ "$CREATE_VENV" == "S" ]]; then
    echo "5. Para activar el entorno virtual en el futuro:"
    if [[ "$OS_TYPE" == "MINGW64_NT" ]] || [[ "$OS_TYPE" == "MSYS_NT" ]]; then
        echo "   source venv/Scripts/activate"
    else
        echo "   source venv/bin/activate"
    fi
    echo ""
fi

echo "📖 Comandos útiles:"
echo "   make help              - Ver todos los comandos disponibles"
echo "   make test              - Ejecutar pruebas"
echo "   make run               - Generar PDF"
echo "   make clean             - Limpiar archivos generados"
echo ""

print_success "¡Instalación completada exitosamente!"
echo ""
echo "Para más información, visita:"
echo "https://github.com/gloriaperaltav/email-to-pdf-generator"
echo ""
