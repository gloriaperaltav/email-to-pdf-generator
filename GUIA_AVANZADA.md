# Guía Avanzada - Email to PDF Generator 🚀

Esta guía cubre temas avanzados de personalización y uso del generador de PDF.

## Tabla de Contenidos

1. [Personalización de Estilos](#personalización-de-estilos)
2. [Uso Programático](#uso-programático)
3. [Integración con APIs](#integración-con-apis)
4. [Optimización de Rendimiento](#optimización-de-rendimiento)
5. [Solución de Problemas Avanzada](#solución-de-problemas-avanzada)

---

## Personalización de Estilos

### Cambiar Colores Corporativos

Edita el archivo `config.py`:

```python
COLORS = {
    'primary': '#1a5490',      # Tu color primario
    'secondary': '#2d7ab8',    # Tu color secundario
    'accent': '#ff6b35',       # Tu color de acentos
    'text': '#2c3e50',
    'light_text': '#7f8c8d',
    'border': '#ecf0f1',
    'background': '#fafafa',
}
```

### Cambiar Tipografía

```python
FONTS = {
    'family': "'Arial', 'Helvetica', sans-serif",  # Cambiar fuente
    'size_body': '11pt',       # Aumentar tamaño
    'size_header': '15pt',
    'size_title': '40pt',
    'size_subtitle': '18pt',
    'size_toc': '20pt',
    'line_height': '1.8',      # Aumentar espaciado
}
```

### Ajustar Márgenes

```python
MARGINS = {
    'top': '3cm',      # Aumentar margen superior
    'right': '2.5cm',
    'bottom': '3cm',
    'left': '2.5cm',
}
```

---

## Uso Programático

### Importar como Módulo

```python
from generar_pdf_correos import generate_pdf

# Definir correos
correos = [
    {
        "from": "usuario@example.com",
        "subject": "Asunto del correo",
        "date": "2026-09-25",
        "body": "Contenido del correo",
        "attachments": []
    }
]

# Generar PDF
generate_pdf(correos, output_file="mi_reporte.pdf")
```

### Usar con Datos Dinámicos

```python
import json
from datetime import datetime
from generar_pdf_desde_json import generate_pdf_from_json

# Cargar correos desde API
import requests

response = requests.get('https://api.example.com/emails')
emails = response.json()

# Guardar a JSON temporal
with open('temp_emails.json', 'w') as f:
    json.dump(emails, f)

# Generar PDF
generate_pdf_from_json('temp_emails.json', 'reporte_dinamico.pdf')
```

### Crear Función Personalizada

```python
from jinja2 import Template
from weasyprint import HTML
from pathlib import Path

def generate_custom_pdf(emails, config):
    """Genera PDF con configuración personalizada."""
    
    # Plantilla personalizada
    template_str = """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body { font-family: {{ config.font }}; }
            .header { color: {{ config.primary_color }}; }
        </style>
    </head>
    <body>
        {% for email in emails %}
        <div class="email">
            <div class="header">{{ email.subject }}</div>
            <div class="body">{{ email.body }}</div>
        </div>
        {% endfor %}
    </body>
    </html>
    """
    
    template = Template(template_str)
    html_content = template.render(emails=emails, config=config)
    
    HTML(string=html_content).write_pdf('custom_output.pdf')

# Usar
config = {
    'font': 'Arial',
    'primary_color': '#2c3e50'
}
generate_custom_pdf(emails, config)
```

---

## Integración con APIs

### Integración con Gmail API

```python
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import base64
import json

def get_emails_from_gmail(num_emails=5):
    """Obtiene correos de Gmail y los convierte al formato esperado."""
    
    # Autenticación (requiere credenciales de Google)
    SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
    
    # ... código de autenticación ...
    
    service = build('gmail', 'v1', credentials=creds)
    results = service.users().messages().list(userId='me', maxResults=num_emails).execute()
    
    emails = []
    for msg in results.get('messages', []):
        message = service.users().messages().get(userId='me', id=msg['id']).execute()
        headers = message['payload']['headers']
        
        email_data = {
            'from': next(h['value'] for h in headers if h['name'] == 'From'),
            'subject': next(h['value'] for h in headers if h['name'] == 'Subject'),
            'date': next(h['value'] for h in headers if h['name'] == 'Date'),
            'body': message['snippet'],
            'attachments': []
        }
        emails.append(email_data)
    
    return emails

# Usar
emails = get_emails_from_gmail(5)
with open('gmail_emails.json', 'w') as f:
    json.dump(emails, f)
```

### Integración con Sentry

```python
import requests

def get_emails_from_sentry(org_slug, api_token):
    """Obtiene alertas de Sentry y las convierte a formato de correo."""
    
    headers = {'Authorization': f'Bearer {api_token}'}
    url = f'https://sentry.io/api/0/organizations/{org_slug}/issues/'
    
    response = requests.get(url, headers=headers)
    issues = response.json()
    
    emails = []
    for issue in issues:
        email_data = {
            'from': 'Sentry <alerts@sentry.io>',
            'subject': f"[{issue['project']['name']}] {issue['title']}",
            'date': issue['lastSeen'],
            'body': issue['metadata'].get('value', issue['title']),
            'attachments': []
        }
        emails.append(email_data)
    
    return emails
```

---

## Optimización de Rendimiento

### Generar PDFs en Lotes

```python
from concurrent.futures import ThreadPoolExecutor
import os

def generate_pdfs_batch(email_groups, output_dir='pdfs'):
    """Genera múltiples PDFs en paralelo."""
    
    os.makedirs(output_dir, exist_ok=True)
    
    def generate_single(group_name, emails):
        output_file = f"{output_dir}/{group_name}.pdf"
        generate_pdf_from_json(emails, output_file)
        return output_file
    
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [
            executor.submit(generate_single, name, emails)
            for name, emails in email_groups.items()
        ]
        results = [f.result() for f in futures]
    
    return results

# Usar
email_groups = {
    'errors': errors_emails,
    'warnings': warnings_emails,
    'info': info_emails,
}
generate_pdfs_batch(email_groups)
```

### Cachear Resultados

```python
import hashlib
import pickle
from pathlib import Path

def generate_pdf_cached(emails, output_file='correos.pdf', cache_dir='.cache'):
    """Genera PDF con caché para evitar regeneración."""
    
    Path(cache_dir).mkdir(exist_ok=True)
    
    # Crear hash de los datos
    data_str = str(emails)
    data_hash = hashlib.md5(data_str.encode()).hexdigest()
    cache_file = Path(cache_dir) / f"{data_hash}.pdf"
    
    if cache_file.exists():
        print(f"✓ Usando PDF en caché: {cache_file}")
        cache_file.rename(output_file)
        return True
    
    # Generar nuevo PDF
    generate_pdf_from_json(emails, output_file)
    
    # Guardar en caché
    Path(output_file).rename(cache_file)
    cache_file.rename(output_file)
    
    return True
```

---

## Solución de Problemas Avanzada

### Depuración de Plantillas

```python
from jinja2 import Template, DebugUndefined

# Usar DebugUndefined para ver variables no definidas
template = Template(html_content, undefined=DebugUndefined)
html_output = template.render(emails=emails)

# Guardar HTML para inspeccionar
with open('debug_output.html', 'w') as f:
    f.write(html_output)
```

### Validar JSON

```python
import json
from jsonschema import validate, ValidationError

schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "from": {"type": "string"},
            "subject": {"type": "string"},
            "date": {"type": "string"},
            "body": {"type": "string"},
            "attachments": {"type": "array"}
        },
        "required": ["from", "subject", "date", "body"]
    }
}

def validate_emails_json(json_file):
    """Valida que el JSON cumpla con el esquema."""
    with open(json_file) as f:
        data = json.load(f)
    
    try:
        validate(instance=data, schema=schema)
        print("✓ JSON válido")
        return True
    except ValidationError as e:
        print(f"✗ Error de validación: {e.message}")
        return False
```

### Logging Detallado

```python
import logging

# Configurar logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('pdf_generator.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

def generate_pdf_with_logging(emails, output_file):
    """Genera PDF con logging detallado."""
    
    logger.info(f"Iniciando generación de PDF con {len(emails)} correos")
    
    try:
        logger.debug(f"Renderizando plantilla...")
        template = Template(HTML_TEMPLATE)
        html_content = template.render(emails=emails)
        logger.debug(f"Plantilla renderizada: {len(html_content)} caracteres")
        
        logger.debug(f"Generando PDF...")
        HTML(string=html_content).write_pdf(output_file)
        
        file_size = Path(output_file).stat().st_size
        logger.info(f"PDF generado exitosamente: {output_file} ({file_size} bytes)")
        
    except Exception as e:
        logger.error(f"Error al generar PDF: {e}", exc_info=True)
        raise
```

---

## Ejemplos Completos

### Ejemplo 1: Generar PDF desde Base de Datos

```python
import sqlite3
import json
from generar_pdf_desde_json import generate_pdf_from_json

def generate_pdf_from_db(db_file, output_pdf):
    """Genera PDF a partir de correos en base de datos SQLite."""
    
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT from_addr, subject, date, body 
        FROM emails 
        ORDER BY date DESC 
        LIMIT 5
    ''')
    
    emails = []
    for row in cursor.fetchall():
        emails.append({
            'from': row[0],
            'subject': row[1],
            'date': row[2],
            'body': row[3],
            'attachments': []
        })
    
    # Guardar a JSON temporal
    with open('temp.json', 'w') as f:
        json.dump(emails, f)
    
    # Generar PDF
    generate_pdf_from_json('temp.json', output_pdf)
    
    conn.close()

# Usar
generate_pdf_from_db('emails.db', 'reporte.pdf')
```

### Ejemplo 2: Generar PDF con Filtros

```python
def generate_filtered_pdf(emails, filter_func, output_file):
    """Genera PDF solo con correos que cumplen el filtro."""
    
    filtered_emails = [e for e in emails if filter_func(e)]
    
    with open('filtered.json', 'w') as f:
        json.dump(filtered_emails, f)
    
    generate_pdf_from_json('filtered.json', output_file)

# Usar - solo correos de error
generate_filtered_pdf(
    emails,
    lambda e: 'error' in e['subject'].lower(),
    'errores.pdf'
)
```

---

## Recursos Adicionales

- [Documentación de Jinja2](https://jinja.palletsprojects.com/)
- [Documentación de WeasyPrint](https://weasyprint.org/)
- [Referencia CSS para PDF](https://weasyprint.org/docs/features/)
- [Google Gmail API](https://developers.google.com/gmail/api)
- [Sentry API](https://docs.sentry.io/api/)

---

**¿Necesitas ayuda?** Abre un issue en el repositorio.
