"""
Archivo de configuración para personalizar los estilos del PDF.
Modifica estos valores para cambiar la apariencia del documento generado.
"""

# Colores
COLORS = {
    'primary': '#2c3e50',      # Color principal (gris oscuro)
    'secondary': '#34495e',    # Color secundario
    'accent': '#3498db',       # Color de acentos (azul)
    'text': '#333333',         # Color del texto
    'light_text': '#7f8c8d',   # Texto claro
    'border': '#ecf0f1',       # Color de bordes
    'background': '#fafafa',   # Fondo de cuerpo
}

# Tipografía
FONTS = {
    'family': "'Segoe UI', Tahoma, Geneva, Verdana, sans-serif",
    'size_body': '10pt',
    'size_header': '14pt',
    'size_title': '36pt',
    'size_subtitle': '16pt',
    'size_toc': '18pt',
    'line_height': '1.6',
}

# Márgenes (en cm)
MARGINS = {
    'top': '2cm',
    'right': '2cm',
    'bottom': '2cm',
    'left': '2cm',
}

# Tamaño de página
PAGE = {
    'size': 'A4',
    'orientation': 'portrait',
}

# Espaciado
SPACING = {
    'section_margin': '1cm',
    'item_margin': '0.5cm',
    'padding_header': '1.5cm',
    'padding_body': '1.5cm',
}

# Metadatos del documento
DOCUMENT = {
    'title': 'Correos Gmail',
    'subtitle': 'Reporte de mensajes',
    'language': 'es',
    'encoding': 'UTF-8',
}

# Configuración de tabla de contenidos
TOC = {
    'enabled': True,
    'title': '📑 Tabla de Contenidos',
    'max_subject_length': 60,
}

# Configuración de portada
COVER = {
    'enabled': True,
    'title': '📧 Correos Gmail',
    'show_metadata': True,
}

# Configuración de numeración de páginas
PAGINATION = {
    'enabled': True,
    'format': 'Página {page} de {pages}',
    'position': 'bottom-center',
    'font_size': '10pt',
}

# Configuración de correos
EMAIL = {
    'page_break_after': True,
    'show_attachments': False,
    'max_body_preview': None,  # None = mostrar todo
}

# Estilos de sombra
SHADOWS = {
    'enabled': True,
    'blur': '4px',
    'offset': '2px',
    'color': 'rgba(0,0,0,0.1)',
}

# Bordes
BORDERS = {
    'email_border': '1px solid #ecf0f1',
    'email_border_radius': '4px',
    'header_border_bottom': '3px solid #3498db',
    'toc_border_bottom': '2px solid #3498db',
}

# Gradientes
GRADIENTS = {
    'header': 'linear-gradient(135deg, #2c3e50 0%, #34495e 100%)',
    'separator': 'linear-gradient(to right, #ecf0f1, #3498db, #ecf0f1)',
}

# Configuración de impresión
PRINT = {
    'background_color': 'white',
    'remove_shadows': False,
    'optimize_for_print': True,
}

# Función auxiliar para generar CSS personalizado
def get_custom_css():
    """Genera CSS personalizado basado en la configuración."""
    css = f"""
    :root {{
        --primary-color: {COLORS['primary']};
        --secondary-color: {COLORS['secondary']};
        --accent-color: {COLORS['accent']};
        --text-color: {COLORS['text']};
        --light-text: {COLORS['light_text']};
        --border-color: {COLORS['border']};
        --background-color: {COLORS['background']};
    }}
    
    body {{
        font-family: {FONTS['family']};
        font-size: {FONTS['size_body']};
        line-height: {FONTS['line_height']};
        color: {COLORS['text']};
    }}
    
    @page {{
        size: {PAGE['size']};
        margin: {MARGINS['top']} {MARGINS['right']} {MARGINS['bottom']} {MARGINS['left']};
    }}
    """
    return css

if __name__ == "__main__":
    print("Configuración cargada correctamente")
    print(f"Color primario: {COLORS['primary']}")
    print(f"Fuente: {FONTS['family']}")
    print(f"Márgenes: {MARGINS}")
