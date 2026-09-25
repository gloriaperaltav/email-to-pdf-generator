# Email to PDF Generator 📧➡️📄

Script Python para generar un PDF profesional a partir de correos Gmail usando **Jinja2** y **WeasyPrint**.

## Características ✨

- ✅ **Portada profesional** con metadatos
- ✅ **Tabla de contenidos** automática
- ✅ **Encabezados claros** con remitente, asunto y fecha
- ✅ **Separadores visuales** entre correos
- ✅ **Numeración de páginas** automática
- ✅ **Formato A4** con márgenes de 2cm
- ✅ **Tipografía clara y legible**
- ✅ **Saltos de página** entre correos
- ✅ **Estilos profesionales** con gradientes y colores corporativos

## Requisitos 📋

- Python 3.7+
- pip (gestor de paquetes de Python)

## Instalación 🔧

### 1. Clonar el repositorio
```bash
git clone https://github.com/gloriaperaltav/email-to-pdf-generator.git
cd email-to-pdf-generator
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

O instalar manualmente:
```bash
pip install jinja2==3.1.2 weasyprint==60.1
```

### Nota para usuarios de macOS
Si tienes problemas con WeasyPrint en macOS, instala las dependencias del sistema:
```bash
brew install python3 cairo pango gdk-pixbuf libffi
```

## Uso 🚀

### Ejecución básica
```bash
python generar_pdf_correos.py
```

El script generará un archivo `correos_gmail.pdf` en el directorio actual.

### Personalizar los correos
Edita la variable `CORREOS_DATA` en el archivo `generar_pdf_correos.py` con tus propios correos:

```python
CORREOS_DATA = [
  {
    "from": "Remitente <email@example.com>",
    "subject": "Asunto del correo",
    "date": "2026-09-25",
    "body": "Cuerpo del mensaje...",
    "attachments": []
  },
  # ... más correos
]
```

## Estructura del PDF 📑

El PDF generado incluye:

1. **Portada** - Título, fecha de generación y metadatos
2. **Tabla de Contenidos** - Listado de todos los correos
3. **Correos** - Cada correo en una página separada con:
   - Número de correo (círculo azul)
   - Asunto
   - Remitente
   - Fecha
   - Cuerpo del mensaje

## Ejemplo de salida 📊

```
✅ PDF generado exitosamente
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📄 Archivo: correos_gmail.pdf
📊 Número de páginas: ~7
💾 Tamaño del archivo: 0.45 MB (456,789 bytes)
📧 Correos incluidos: 5
📅 Fecha de generación: 25 de September de 2026 a las 23:55:39
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## Tecnologías utilizadas 🛠️

- **Jinja2** - Motor de plantillas HTML
- **WeasyPrint** - Generador de PDF desde HTML/CSS
- **Python 3** - Lenguaje de programación

## Estructura del proyecto 📁

```
email-to-pdf-generator/
├── generar_pdf_correos.py    # Script principal
├── requirements.txt           # Dependencias del proyecto
├── README.md                  # Este archivo
└── correos_gmail.pdf          # PDF generado (después de ejecutar)
```

## Solución de problemas 🔍

### Error: "No module named 'jinja2'"
```bash
pip install jinja2
```

### Error: "No module named 'weasyprint'"
```bash
pip install weasyprint
```

### Error en macOS: "ImportError: cannot import name 'Pixbuf'"
Instala las dependencias del sistema:
```bash
brew install cairo pango gdk-pixbuf libffi
pip install --upgrade weasyprint
```

### El PDF se genera pero sin estilos
Asegúrate de que WeasyPrint esté correctamente instalado:
```bash
pip install --upgrade weasyprint
```

## Personalización avanzada 🎨

### Cambiar colores
Edita los valores de color en la sección `<style>` de `HTML_TEMPLATE`:
- `#2c3e50` - Color principal (gris oscuro)
- `#3498db` - Color de acentos (azul)
- `#34495e` - Color secundario

### Cambiar fuente
Modifica la propiedad `font-family` en el CSS:
```css
font-family: 'Arial', sans-serif;  /* Cambiar a Arial */
```

### Ajustar márgenes
Modifica la regla `@page` en el CSS:
```css
@page {
    margin: 3cm;  /* Cambiar a 3cm */
}
```

## Licencia 📜

Este proyecto está disponible bajo la licencia MIT.

## Autor ✍️

Creado por Gloria Peralta - 2026

## Contribuciones 🤝

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request.

---

**¿Necesitas ayuda?** Abre un issue en el repositorio.
