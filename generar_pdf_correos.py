#!/usr/bin/env python3
"""
Script para generar un PDF profesional a partir de correos Gmail.
Utiliza Jinja2 para plantillas HTML y WeasyPrint para la generación del PDF.

Dependencias:
    pip install jinja2 weasyprint
"""

import json
import os
from datetime import datetime
from pathlib import Path
from jinja2 import Template
from weasyprint import HTML, CSS
from io import BytesIO

# Datos de entrada (5 correos Gmail)
CORREOS_DATA = [
  {
    "from": "Sentry Orion <sentry@cloud.orion.global>",
    "subject": "[Sentry] KERNEL-FRONTEND-P6 - AxiosError: No se pudo completar la operación (error 500).",
    "date": "2026-09-25",
    "body": "Details\n-------\n\nhttps://sentry.cloud.orion.global/organizations/orion/issues/635/?referrer=alert_email&alert_type=email&alert_timestamp=1790380157393&alert_rule_id=3&notification_uuid=f238acf4-caf5-4392-98c5-6a9d79ced264&environment=production\n\n\nTags\n----\n\n* area = axios\n* browser = Chrome 154.0.0\n* browser.name = Chrome\n* device = Mac\n* device.family = Mac\n* environment = production\n* handled = yes\n* http.method = POST\n* http.status_code = 500\n* interface_type = exception\n* level = error\n* mechanism = generic\n* os = Mac OS X >=10.15.7\n* os.name = Mac OS X\n* replayId = 4d6f645233174eb1bcf80382a68d8331\n* sentry:release = 206f2395a75b36dac23c3398e38d2903143a089d\n* transaction = /auth/google/callback\n* url = /api/auth/google/\n\n\nException\n-----------\n\nAxiosError: No se pudo completar la operación (error 500).\n  at j_ (/assets/app-core-dVO-ihdx.js:7:10327)\n  at XMLHttpRequest.g (/assets/app-core-dVO-ihdx.js:7:16451)\n\n\nRequest\n-----------",
    "attachments": []
  },
  {
    "from": "Sentry Orion <sentry@cloud.orion.global>",
    "subject": "[Sentry] KERNEL-BACKEND-WM - MasterNotFoundError: No master found for 'mymaster'",
    "date": "2026-09-25",
    "body": "Details\n-------\n\nhttps://sentry.cloud.orion.global/organizations/orion/issues/634/?referrer=alert_email&alert_type=email&alert_timestamp=1790380155291&alert_rule_id=2&notification_uuid=b4208a55-1ace-421d-a6b8-173b8f422fcf&environment=production\n\n\nTags\n----\n\n* area = drf\n* browser = Chrome 154\n* browser.name = Chrome\n* client_os = macOS\n* client_os.name = macOS\n* component = auth\n* device = Mac\n* device.family = Mac\n* drf.handled = false\n* environment = production\n* handled = yes\n* http.method = POST\n* interface_type = exception\n* level = error\n* mechanism = generic\n* runtime = CPython 3.13.15\n* runtime.name = CPython\n* sentry:release = 8d1d78a7ae47a92c1ac4261c343ce6f9427043f0\n* server_name = app-orion-django-langraph-backend-master-5868d88d85-9655f\n* transaction = /api/auth/google/\n* url = https://app.getkrnl.ai/api/auth/google/\n* view = GoogleAuthView\n\n\nException\n-----------\n\nConnectionInterrupted: Redis MasterNotFoundError: No master found for 'mymaster'\n  File \"django_redis/cache.py\", line 48, in _decorator\n    return method(self, *args, **kwargs)\n  File \"django_redis/cache.py\", line 129, in delete\n    return bool(self.client.delete(*args, **kwargs))\n  File \"django_redis/client/default.py\", line 495, in delete\n    raise ConnectionInterrupted(connection=client) from e\n\nMasterNotFoundError: No master found for 'mymaster'\n(17 additional frame(s) were not displayed)\n...\n  File \"users/views.py\", line 783, in post\n    update_last_login(None, user)\n  File \"users/signals.py\", line 34, in invalidate_user_model_cache\n    invalidate_user_cache(instance.id)\n  File \"users/signals.py\", line 28, in invalidate_user_cache\n    cache.delete(cache_key)",
    "attachments": []
  },
  {
    "from": "Sentry Orion <sentry@cloud.orion.global>",
    "subject": "[Sentry] KERNEL-BACKEND-WK - TemplateRenderError: expected name or number",
    "date": "2026-09-25",
    "body": "Details\n-------\n\nhttps://sentry.cloud.orion.global/organizations/orion/issues/633/?referrer=alert_email&alert_type=email&alert_timestamp=1790378542351&alert_rule_id=2&notification_uuid=e5b77e84-87b9-4142-bb12-85301f1df2b4&environment=development\n\n\nTags\n----\n\n* area = workflow-engine\n* celery_task_id = 2a729a6f-aa46-40a4-9526-0f70dfdd79b5\n* component = workflows.execute_workflow_run\n* environment = development\n* handled = yes\n* interface_type = exception\n* level = error\n* mechanism = generic\n* run_id = 4c7afd28-f644-4a17-a4ef-2bc7cfa9a64f\n* runtime = CPython 3.13.15\n* runtime.name = CPython\n* sentry:release = d270ffe337f4f9697521ba1f532d4163b519b0f7\n* server_name = app-orion-django-langraph-backend-celery-worker-develop-wot52m6\n* transaction = workflows.execute_workflow_run\n* workflow_id = 60c10eef-acf6-44d2-8d07-1547d61a7d36\n\n\nException\n-----------\n\nTemplateRenderError: expected name or number\n  File \"workflows/engine/executor.py\", line 380, in run_async\n    await asyncio.wait_for(traversal, timeout=limits.RUN_MAX_SECONDS)\n  File \"workflows/engine/executor.py\", line 574, in _traverse\n    rendered_node = render_value_isolated(node, ctx.to_template_context())\n  File \"workflows/engine/templating.py\", line 451, in render_value_isolated\n    _raise_failure(result, value)\n  File \"workflows/engine/templating.py\", line 442, in _raise_failure\n    raise TemplateRenderError(result[\"message\"], template=template)",
    "attachments": []
  },
  {
    "from": "Sentry Orion <sentry@cloud.orion.global>",
    "subject": "[Sentry] KERNEL-BACKEND-WJ - ValueError: JSON inválido: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)",
    "date": "2026-09-25",
    "body": "Details\n-------\n\nhttps://sentry.cloud.orion.global/organizations/orion/issues/632/?referrer=alert_email&alert_type=email&alert_timestamp=1790378197993&alert_rule_id=2&notification_uuid=5767eb66-26c2-43c0-9b50-0cfc6968c796&environment=development\n\n\nTags\n----\n\n* area = workflow-engine\n* celery_task_id = 68b17af9-a4e8-4f27-8127-1e85f767d274\n* component = workflows.execute_workflow_run\n* environment = development\n* handled = yes\n* interface_type = exception\n* level = error\n* mechanism = generic\n* run_id = a8b846bc-66c7-49e5-a8f2-1084a0471f20\n* runtime = CPython 3.13.15\n* runtime.name = CPython\n* sentry:release = d270ffe337f4f9697521ba1f532d4163b519b0f7\n* server_name = app-orion-django-langraph-backend-celery-worker-develop-wot52m6\n* transaction = workflows.execute_workflow_run\n* workflow_id = 60c10eef-acf6-44d2-8d07-1547d61a7d36\n\n\nException\n-----------\n\nJSONDecodeError: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)\n  File \"workflows/engine/runners/advanced.py\", line 62, in run_data_parse_json\n    parsed = json.loads(source) if source.strip() else None\n\nValueError: JSON inválido: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)\n  File \"workflows/engine/executor.py\", line 380, in run_async\n    await asyncio.wait_for(traversal, timeout=limits.RUN_MAX_SECONDS)\n  File \"workflows/engine/executor.py\", line 593, in _traverse\n    result = await asyncio.wait_for(\n  File \"workflows/engine/runners/advanced.py\", line 64, in run_data_parse_json\n    raise ValueError(f\"JSON inválido: {exc}\") from exc",
    "attachments": []
  },
  {
    "from": "Sentry Orion <sentry@cloud.orion.global>",
    "subject": "[Sentry] KERNEL-BACKEND-WH - TimeoutError",
    "date": "2026-09-25",
    "body": "Details\n-------\n\nhttps://sentry.cloud.orion.global/organizations/orion/issues/631/?referrer=alert_email&alert_type=email&alert_timestamp=1790376564594&alert_rule_id=2&notification_uuid=937a3934-e70e-4d30-a994-7fd3b2cc4b0a&environment=development\n\n\nTags\n----\n\n* area = workflow-engine\n* celery_task_id = 31eccb54-7c6a-479c-8b45-779c1766e1e9\n* component = workflows.execute_workflow_run\n* environment = development\n* handled = yes\n* interface_type = exception\n* level = error\n* mechanism = generic\n* run_id = edd4b34a-1f6e-4ff7-ab8c-06e711074e6e\n* runtime = CPython 3.13.15\n* runtime.name = CPython\n* sentry:release = d270ffe337f4f9697521ba1f532d4163b519b0f7\n* server_name = app-orion-django-langraph-backend-celery-worker-develop-wot52m6\n* transaction = workflows.execute_workflow_run\n* workflow_id = 60c10eef-acf6-44d2-8d07-1547d61a7d36\n\n\nException\n-----------\n\nCancelledError: \nCancelledError: \n  File \"workflows/engine/runners/agents.py\", line 269, in run_agent_llm\n    turn = await _turn()\n\nTimeoutError: \n  File \"workflows/engine/executor.py\", line 380, in run_async\n    await asyncio.wait_for(traversal, timeout=limits.RUN_MAX_SECONDS)\n  File \"workflows/engine/executor.py\", line 593, in _traverse\n    result = await asyncio.wait_for(",
    "attachments": []
  }
]

# Plantilla HTML con Jinja2
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Correos Gmail - 5 mensajes</title>
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
            <p class="subtitle">Reporte de 5 mensajes</p>
            <div class="separator"></div>
            <div class="meta">
                <p><strong>Fecha de generación:</strong> {{ generation_date }}</p>
                <p><strong>Total de correos:</strong> {{ emails|length }}</p>
                <p><strong>Remitente:</strong> Sentry Orion</p>
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

def generate_pdf():
    """Genera el PDF a partir de los correos."""
    try:
        # Preparar datos
        generation_date = datetime.now().strftime("%d de %B de %Y a las %H:%M:%S")
        
        # Renderizar plantilla HTML
        template = Template(HTML_TEMPLATE)
        html_content = template.render(
            emails=CORREOS_DATA,
            generation_date=generation_date
        )
        
        # Generar PDF
        output_path = Path("correos_gmail.pdf")
        HTML(string=html_content).write_pdf(str(output_path))
        
        # Obtener información del archivo
        file_size = output_path.stat().st_size
        file_size_mb = file_size / (1024 * 1024)
        
        # Contar páginas aproximadamente (estimación)
        num_pages = len(CORREOS_DATA) + 2  # +2 por portada y tabla de contenidos
        
        # Mensaje de éxito
        success_message = f"""
✅ PDF generado exitosamente
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📄 Archivo: correos_gmail.pdf
📊 Número de páginas: ~{num_pages}
💾 Tamaño del archivo: {file_size_mb:.2f} MB ({file_size:,} bytes)
📧 Correos incluidos: {len(CORREOS_DATA)}
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

if __name__ == "__main__":
    print("🚀 Iniciando generación de PDF de correos Gmail...")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    success = generate_pdf()
    exit(0 if success else 1)
