# 🚀 Inicio Rápido

Sigue estos pasos para empezar a generar PDFs de correos en menos de 5 minutos.

## Paso 1: Clonar el Repositorio

```bash
git clone https://github.com/gloriaperaltav/email-to-pdf-generator.git
cd email-to-pdf-generator
```

## Paso 2: Instalar Dependencias

```bash
pip install -r requirements.txt
```

**Nota para macOS:** Si tienes problemas, instala primero:
```bash
brew install cairo pango gdk-pixbuf libffi
```

## Paso 3: Ejecutar las Pruebas

```bash
python test_generator.py
```

Deberías ver algo como:
```
✅ ¡TODAS LAS PRUEBAS PASARON!
```

## Paso 4: Generar tu Primer PDF

### Opción A: Usar los datos de ejemplo

```bash
python generar_pdf_correos.py
```

Esto generará `correos_gmail.pdf` con los 5 correos de ejemplo.

### Opción B: Usar tus propios correos

1. Edita `ejemplo_correos.json` con tus correos
2. Ejecuta:
```bash
python generar_pdf_desde_json.py ejemplo_correos.json
```

## Paso 5: Personalizar (Opcional)

Edita `config.py` para cambiar:
- **Colores**: `COLORS`
- **Fuentes**: `FONTS`
- **Márgenes**: `MARGINS`

Ejemplo:
```python
COLORS = {
    'primary': '#ff6b35',      # Tu color
    'accent': '#004e89',
    # ...
}
```

---

## Comandos Útiles

### Generar PDF desde JSON personalizado
```bash
python generar_pdf_desde_json.py mis_correos.json -o mi_reporte.pdf
```

### Ver ayuda
```bash
python generar_pdf_desde_json.py --help
```

### Ejecutar pruebas
```bash
python test_generator.py
```

---

## Estructura de Datos

Tu JSON debe tener este formato:

```json
[
  {
    "from": "Remitente <email@example.com>",
    "subject": "Asunto del correo",
    "date": "2026-09-25",
    "body": "Contenido del correo...",
    "attachments": []
  }
]
```

---

## Ejemplos de Uso

### Generar PDF con 5 correos
```bash
python generar_pdf_correos.py
```

### Generar PDF desde archivo JSON
```bash
python generar_pdf_desde_json.py correos.json
```

### Generar PDF con nombre personalizado
```bash
python generar_pdf_desde_json.py correos.json -o reporte_mensual.pdf
```

---

## Solución Rápida de Problemas

### Error: "No module named 'jinja2'"
```bash
pip install jinja2
```

### Error: "No module named 'weasyprint'"
```bash
pip install weasyprint
```

### El PDF se genera pero sin estilos
```bash
pip install --upgrade weasyprint
```

### En macOS: Error de importación
```bash
brew install cairo pango gdk-pixbuf libffi
pip install --upgrade weasyprint
```

---

## Próximos Pasos

- 📖 Lee la [Guía Completa](README.md)
- 🎨 Consulta la [Guía Avanzada](GUIA_AVANZADA.md) para personalización
- 🔧 Modifica `config.py` para tus estilos corporativos
- 🚀 Integra con tus APIs (Gmail, Sentry, etc.)

---

## Soporte

¿Necesitas ayuda?
- 📋 Abre un [issue](https://github.com/gloriaperaltav/email-to-pdf-generator/issues)
- 💬 Revisa la [Guía Avanzada](GUIA_AVANZADA.md)
- 📚 Consulta la [documentación de WeasyPrint](https://weasyprint.org/)

---

**¡Listo!** Ya puedes generar PDFs profesionales de correos. 🎉
