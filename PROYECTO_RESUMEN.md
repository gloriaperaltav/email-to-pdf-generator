# 📊 Resumen del Proyecto - Email to PDF Generator

## 🎯 Objetivo

Crear un script Python profesional que genere PDFs de alta calidad a partir de correos Gmail, utilizando **Jinja2** para plantillas HTML y **WeasyPrint** para la generación de PDFs.

---

## ✅ Requisitos Completados

### 1. **Funcionalidad Principal**
- ✅ Script Python que crea PDF a partir de 5 correos Gmail
- ✅ Datos de entrada en formato JSON
- ✅ Archivo PDF generado: `correos_gmail.pdf`
- ✅ Mensaje de éxito con información del archivo

### 2. **Estructura del PDF**
- ✅ Título: "Correos Gmail - 5 mensajes"
- ✅ Fecha de generación: 2026-09-25
- ✅ Para cada correo:
  - Encabezado con remitente, asunto, fecha
  - Separador visual
  - Cuerpo del mensaje
  - Salto de página (excepto el último)
- ✅ Formato profesional con márgenes
- ✅ Tipografía clara y legible
- ✅ Numeración de página
- ✅ Tabla de contenidos

### 3. **Tecnologías Utilizadas**
- ✅ **Jinja2**: Motor de plantillas HTML
- ✅ **WeasyPrint**: Generador de PDF desde HTML/CSS
- ✅ **Python 3**: Lenguaje de programación

### 4. **Características Adicionales**
- ✅ Portada profesional con metadatos
- ✅ Tabla de contenidos automática
- ✅ Estilos profesionales con gradientes
- ✅ Sombras y bordes redondeados
- ✅ Colores corporativos personalizables
- ✅ Márgenes ajustables (2cm por defecto)
- ✅ Formato A4

---

## 📁 Estructura del Proyecto

```
email-to-pdf-generator/
├── generar_pdf_correos.py          # Script principal (datos embebidos)
├── generar_pdf_desde_json.py       # Script alternativo (carga desde JSON)
├── config.py                        # Configuración de estilos
├── test_generator.py                # Script de pruebas
├── requirements.txt                 # Dependencias del proyecto
├── ejemplo_correos.json             # Archivo JSON de ejemplo
├── README.md                        # Documentación completa
├── QUICKSTART.md                    # Guía de inicio rápido
├── GUIA_AVANZADA.md                # Guía avanzada de personalización
├── PROYECTO_RESUMEN.md             # Este archivo
├── .gitignore                       # Archivos a ignorar en Git
└── correos_gmail.pdf               # PDF generado (después de ejecutar)
```

---

## 🚀 Cómo Usar

### Instalación Rápida

```bash
# 1. Clonar repositorio
git clone https://github.com/gloriaperaltav/email-to-pdf-generator.git
cd email-to-pdf-generator

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Ejecutar pruebas
python test_generator.py

# 4. Generar PDF
python generar_pdf_correos.py
```

### Uso Básico

```bash
# Generar PDF con datos de ejemplo
python generar_pdf_correos.py

# Generar PDF desde archivo JSON
python generar_pdf_desde_json.py ejemplo_correos.json

# Generar PDF con nombre personalizado
python generar_pdf_desde_json.py correos.json -o mi_reporte.pdf
```

---

## 📊 Características del PDF Generado

### Portada
- Título principal: "📧 Correos Gmail"
- Subtítulo: "Reporte de 5 mensajes"
- Metadatos:
  - Fecha de generación
  - Total de correos
  - Remitente principal

### Tabla de Contenidos
- Listado numerado de todos los correos
- Primeros 60 caracteres del asunto
- Navegación visual

### Correos
- Número de correo en círculo azul
- Asunto completo
- Remitente
- Fecha
- Cuerpo del mensaje
- Cada correo en página separada

### Numeración
- Formato: "Página X de Y"
- Posición: Pie de página (centro)
- Automática en todas las páginas

---

## 🎨 Personalización

### Cambiar Colores
Edita `config.py`:
```python
COLORS = {
    'primary': '#2c3e50',      # Color principal
    'accent': '#3498db',       # Color de acentos
    # ... más colores
}
```

### Cambiar Tipografía
```python
FONTS = {
    'family': "'Arial', sans-serif",
    'size_body': '11pt',
    # ... más opciones
}
```

### Ajustar Márgenes
```python
MARGINS = {
    'top': '3cm',
    'right': '2.5cm',
    'bottom': '3cm',
    'left': '2.5cm',
}
```

---

## 📋 Archivos Incluidos

### Scripts Python
1. **generar_pdf_correos.py** (18 KB)
   - Script principal con datos embebidos
   - Genera `correos_gmail.pdf`
   - Ideal para uso rápido

2. **generar_pdf_desde_json.py** (12 KB)
   - Script alternativo con argumentos CLI
   - Carga correos desde archivo JSON
   - Más flexible y reutilizable

3. **config.py** (3.5 KB)
   - Configuración centralizada
   - Personalización de estilos
   - Colores, fuentes, márgenes

4. **test_generator.py** (5.7 KB)
   - Suite de pruebas
   - Valida instalación
   - Verifica estructura

### Documentación
1. **README.md** (4.5 KB)
   - Documentación completa
   - Instalación y uso
   - Solución de problemas

2. **QUICKSTART.md** (3 KB)
   - Guía de inicio rápido
   - Pasos simples
   - Ejemplos básicos

3. **GUIA_AVANZADA.md** (11.4 KB)
   - Personalización avanzada
   - Integración con APIs
   - Optimización de rendimiento

### Datos y Configuración
1. **ejemplo_correos.json** (8.2 KB)
   - Archivo JSON de ejemplo
   - 5 correos de Sentry
   - Formato de referencia

2. **requirements.txt** (31 bytes)
   - Dependencias del proyecto
   - Versiones específicas

3. **.gitignore** (472 bytes)
   - Archivos a ignorar
   - PDFs, caché, logs

---

## 📦 Dependencias

```
jinja2==3.1.2
weasyprint==60.1
```

### Requisitos del Sistema
- Python 3.7+
- pip (gestor de paquetes)
- Para macOS: cairo, pango, gdk-pixbuf, libffi

---

## 🧪 Pruebas

Ejecuta el script de pruebas para validar la instalación:

```bash
python test_generator.py
```

Verifica:
- ✓ Dependencias instaladas
- ✓ Estructura de archivos
- ✓ Validez del JSON
- ✓ Configuración
- ✓ Generación de PDF

---

## 💡 Casos de Uso

1. **Reportes de Errores**
   - Generar PDF con alertas de Sentry
   - Documentar incidentes
   - Compartir con equipo

2. **Archivado de Correos**
   - Guardar correos importantes
   - Crear backups
   - Documentación histórica

3. **Reportes Automáticos**
   - Integrar con APIs
   - Generar reportes diarios
   - Enviar por email

4. **Documentación**
   - Crear manuales
   - Documentar procesos
   - Generar guías

---

## 🔧 Integración con APIs

### Gmail API
```python
from generar_pdf_desde_json import generate_pdf_from_json
# Obtener correos de Gmail
# Guardar a JSON
# Generar PDF
```

### Sentry API
```python
# Obtener alertas de Sentry
# Convertir a formato de correo
# Generar PDF
```

### Bases de Datos
```python
# Consultar correos de BD
# Exportar a JSON
# Generar PDF
```

---

## 📈 Estadísticas del Proyecto

| Métrica | Valor |
|---------|-------|
| Archivos Python | 4 |
| Líneas de código | ~1,500 |
| Documentación | 4 archivos |
| Dependencias | 2 |
| Tamaño total | ~50 KB |
| Tiempo de ejecución | <5 segundos |

---

## 🎓 Aprendizajes

Este proyecto demuestra:
- ✅ Uso de Jinja2 para plantillas
- ✅ Generación de PDF con WeasyPrint
- ✅ Manejo de JSON en Python
- ✅ Argumentos CLI con argparse
- ✅ Buenas prácticas de código
- ✅ Documentación profesional
- ✅ Testing y validación
- ✅ Configuración centralizada

---

## 🚀 Mejoras Futuras

- [ ] Soporte para múltiples idiomas
- [ ] Temas de colores predefinidos
- [ ] Exportación a otros formatos (DOCX, HTML)
- [ ] Interfaz gráfica (GUI)
- [ ] API REST
- [ ] Integración con servicios en la nube
- [ ] Compresión de PDFs
- [ ] Watermarks personalizados

---

## 📞 Soporte

### Documentación
- 📖 [README.md](README.md) - Documentación completa
- 🚀 [QUICKSTART.md](QUICKSTART.md) - Inicio rápido
- 🎓 [GUIA_AVANZADA.md](GUIA_AVANZADA.md) - Temas avanzados

### Recursos Externos
- [Jinja2 Docs](https://jinja.palletsprojects.com/)
- [WeasyPrint Docs](https://weasyprint.org/)
- [Python Docs](https://docs.python.org/)

### Reportar Problemas
- 🐛 [Issues en GitHub](https://github.com/gloriaperaltav/email-to-pdf-generator/issues)

---

## 📄 Licencia

Este proyecto está disponible bajo la licencia MIT.

---

## 👤 Autor

**Gloria Peralta** - 2026

---

## 🙏 Agradecimientos

- Jinja2 por el motor de plantillas
- WeasyPrint por la generación de PDFs
- Python por el lenguaje

---

**Última actualización:** 2026-09-25

**Estado:** ✅ Completado y funcional

**Versión:** 1.0.0
