#!/usr/bin/env python3
"""
Script alternativo para generar PDF a partir de correos cargados desde un archivo JSON.
Permite mayor flexibilidad en la entrada de datos.

Uso:
    python generar_pdf_desde_json.py correos.json
    python generar_pdf_desde_json.py correos.json --output mi_reporte.pdf
"""

import json
import sys
import argparse
from datetime import datetime
from pathlib import Path
from jinja2 import Template
from weasyprint import HTML

# Plantilla HTML (igual que en el script principal)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Correos Gmail - {{ emails|length }} mensajes</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        @page {
            size: A4;
            margin: 2cm;
            @bottom-center {
                content: "Página " counter(page) " de " counter(pages);
                font-size: 10pt;
                color: #666;
            }
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background-color: #f5f5f5;
        }
        
        .container {
            max-width: 210mm;
            margin: 0 auto;
            background-color: white;
            padding: 2cm;
        }
        
        /* Portada */
        .cover-page {
            page-break-after: always;
            text-align: center;
            padding: 5cm 0;
            border-bottom: 3px solid #2c3e50;
            margin-bottom: 2cm;
        }
        
        .cover-page h1 {
            font-size: 36pt;
            color: #2c3e50;
            margin-bottom: 1cm;
            font-weight: 700;
        }
        
        .cover-page .subtitle {
            font-size: 16pt;
            color: #7f8c8d;
            margin-bottom: 2cm;
        }
        
        .cover-page .meta {
            font-size: 12pt;
            color: #95a5a6;
            margin-top: 3cm;
        }
        
        .cover-page .meta p {
            margin: 0.5cm 0;
        }
        
        /* Tabla de contenidos */
        .toc {
            page-break-after: always;
            margin-bottom: 2cm;
        }
        
        .toc h2 {
            font-size: 18pt;
            color: #2c3e50;
            margin-bottom: 1cm;
            border-bottom: 2px solid #3498db;
            padding-bottom: 0.5cm;
        }
        
        .toc-item {
            margin: 0.5cm 0;
            padding-left: 1cm;
            font-size: 11pt;
        }
        
        .toc-item .number {
            color: #3498db;
            font-weight: bold;
            margin-right: 0.5cm;
        }
        
        /* Correos */
        .email {
            page-break-after: always;
            margin-bottom: 2cm;
            border: 1px solid #ecf0f1;
            border-radius: 4px;
            overflow: hidden;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        
        .email:last-child {
            page-break-after: avoid;
        }
        
        .email-header {
            background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
            color: white;
            padding: 1.5cm;
            border-bottom: 3px solid #3498db;
        }
        
        .email-header h2 {
            font-size: 14pt;
            margin-bottom: 0.5cm;
            word-wrap: break-word;
            overflow-wrap: break-word;
        }
        
        .email-meta {
            font-size: 10pt;
            opacity: 0.9;
            margin-top: 0.5cm;
        }
        
        .email-meta-row {
            margin: 0.3cm 0;
        }
        
        .email-meta-label {
            font-weight: bold;
            display: inline-block;
            width: 3cm;
        }
        
        .email-body {
            padding: 1.5cm;
            background-color: #fafafa;
            font-size: 10pt;
            line-height: 1.5;
            white-space: pre-wrap;
            word-wrap: break-word;
            overflow-wrap: break-word;
        }
        
        .email-body a {
            color: #3498db;
            text-decoration: none;
        }
        
        .email-body a:hover {
            text-decoration: underline;
        }
        
        .separator {
            height: 2px;
            background: linear-gradient(to right, #ecf0f1, #3498db, #ecf0f1);
            margin: 1cm 0;
        }
        
        .email-number {
            display: inline-block;
            background-color: #3498db;
            color: white;
            width: 2cm;
            height: 2cm;
            border-radius: 50%;
            text-align: center;
            line-height: 2cm;
            font-weight: bold;
            font-size: 14pt;
            margin-right: 0.5cm;
            vertical-align: middle;
        }
        
        /* Estilos de impresión */
        @media print {
            body {
                background-color: white;
            }
            .container {
                padding: 0;
                box-shadow: none;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- Portada -->
        <div class="cover-page">
            <h1>📧 Correos Gmail</h1>
            <p class="subtitle">Reporte de {{ emails|length }} mensajes</p>
            <div class="separator"></div>
            <div class="meta">
                <p><strong>Fecha de generación:</strong> {{ generation_date }}</p>
                <p><strong>Total de correos:</strong> {{ emails|length }}</p>
                {% if emails|length > 0 %}
                <p><strong>Remitente principal:</strong> {{ emails[0].from }}</p>
                {% endif %}
            </div>
        </div>
        
        <!-- Tabla de contenidos -->
        <div class="toc">
            <h2>📑 Tabla de Contenidos</h2>
            {% for email in emails %}
            <div class="toc-item">
                <span class="number">{{ loop.index }}.</span>
                <span>{{ email.subject[:60] }}{% if email.subject|length > 60 %}...{% endif %}</span>
            </div>
            {% endfor %}
        </div>
        
        <!-- Correos -->
        {% for email in emails %}
        <div class="email">
            <div class="email-header">
                <div style="display: flex; align-items: center;">
                    <span class="email-number">{{ loop.index }}</span>
                    <h2>{{ email.subject }}</h2>
                </div>
                <div class="email-meta">
                    <div class="email-meta-row">
                        <span class="email-meta-label">De:</span>
                        <span>{{ email.from }}</span>
                    </div>
                    <div class="email-meta-row">
                        <span class="email-meta-label">Fecha:</span>
                        <span>{{ email.date }}</span>
                    </div>
                </div>
            </div>
            <div class="email-body">{{ email.body }}</div>
        </div>
        {% endfor %}
    </div>
</body>
</html>
"""

def load_emails_from_json(json_file):
    """Carga correos desde un archivo JSON."""
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Soportar tanto lista directa como objeto con clave 'emails'
        if isinstance(data, list):
            return data
        elif isinstance(data, dict) and 'emails' in data:
            return data['emails']
        else:
            raise ValueError("El JSON debe contener una lista de correos o un objeto con clave 'emails'")
    
    except FileNotFoundError:
        print(f"❌ Error: Archivo no encontrado: {json_file}")
        return None
    except json.JSONDecodeError as e:
        print(f"❌ Error: JSON inválido en {json_file}: {e}")
        return None
    except Exception as e:
        print(f"❌ Error al cargar JSON: {e}")
        return None

def generate_pdf_from_json(json_file, output_file=None):
    """Genera PDF a partir de un archivo JSON con correos."""
    
    # Cargar correos
    emails = load_emails_from_json(json_file)
    if emails is None:
        return False
    
    if not emails:
        print("❌ Error: No se encontraron correos en el archivo JSON")
        return False
    
    try:
        # Preparar datos
        generation_date = datetime.now().strftime("%d de %B de %Y a las %H:%M:%S")
        
        # Renderizar plantilla HTML
        template = Template(HTML_TEMPLATE)
        html_content = template.render(
            emails=emails,
            generation_date=generation_date
        )
        
        # Determinar nombre del archivo de salida
        if output_file is None:
            output_file = "correos_gmail.pdf"
        
        # Generar PDF
        output_path = Path(output_file)
        HTML(string=html_content).write_pdf(str(output_path))
        
        # Obtener información del archivo
        file_size = output_path.stat().st_size
        file_size_mb = file_size / (1024 * 1024)
        
        # Contar páginas aproximadamente
        num_pages = len(emails) + 2  # +2 por portada y tabla de contenidos
        
        # Mensaje de éxito
        success_message = f"""
✅ PDF generado exitosamente
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📄 Archivo: {output_file}
📊 Número de páginas: ~{num_pages}
💾 Tamaño del archivo: {file_size_mb:.2f} MB ({file_size:,} bytes)
📧 Correos incluidos: {len(emails)}
📅 Fecha de generación: {generation_date}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Características del PDF:
  ✓ Portada profesional con metadatos
  ✓ Tabla de contenidos automática
  ✓ Encabezados con remitente, asunto y fecha
  ✓ Separadores visuales entre correos
  ✓ Numeración de páginas
  ✓ Formato A4 con márgenes de 2cm
  ✓ Tipografía clara y legible
  ✓ Saltos de página entre correos
  ✓ Estilos profesionales con gradientes
        """
        
        print(success_message)
        return True
        
    except ImportError as e:
        print(f"❌ Error: Falta instalar dependencias")
        print(f"   Ejecuta: pip install jinja2 weasyprint")
        print(f"   Detalle: {e}")
        return False
    except Exception as e:
        print(f"❌ Error al generar PDF: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Función principal con argumentos de línea de comandos."""
    parser = argparse.ArgumentParser(
        description='Genera un PDF profesional a partir de correos en formato JSON',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:
  python generar_pdf_desde_json.py correos.json
  python generar_pdf_desde_json.py correos.json --output mi_reporte.pdf
  python generar_pdf_desde_json.py datos/emails.json -o salida/reporte.pdf

Formato del archivo JSON:
  [
    {
      "from": "Remitente <email@example.com>",
      "subject": "Asunto del correo",
      "date": "2026-09-25",
      "body": "Cuerpo del mensaje...",
      "attachments": []
    }
  ]
        """
    )
    
    parser.add_argument('json_file', help='Archivo JSON con los correos')
    parser.add_argument('-o', '--output', help='Nombre del archivo PDF de salida (default: correos_gmail.pdf)')
    
    args = parser.parse_args()
    
    print("🚀 Iniciando generación de PDF desde JSON...")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    
    success = generate_pdf_from_json(args.json_file, args.output)
    exit(0 if success else 1)

if __name__ == "__main__":
    main()
