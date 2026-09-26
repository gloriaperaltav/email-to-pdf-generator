# 🤝 Guía de Contribuciones

¡Gracias por tu interés en contribuir a Email to PDF Generator! Este documento proporciona directrices para contribuir al proyecto.

## 📋 Código de Conducta

Por favor, sé respetuoso y constructivo en todas las interacciones. Nos comprometemos a mantener un ambiente inclusivo y acogedor.

## 🐛 Reportar Bugs

Si encuentras un bug, por favor abre un issue con:

1. **Descripción clara** del problema
2. **Pasos para reproducir** el error
3. **Comportamiento esperado** vs **comportamiento actual**
4. **Información del sistema** (OS, Python version, etc.)
5. **Logs o mensajes de error** si están disponibles

### Ejemplo de reporte de bug:

```
Título: PDF no se genera con caracteres especiales

Descripción:
Cuando intento generar un PDF con caracteres especiales (ñ, é, etc.), 
el script falla con un error de codificación.

Pasos para reproducir:
1. Crear un archivo JSON con caracteres especiales
2. Ejecutar: python generar_pdf_desde_json.py archivo.json
3. Observar el error

Error:
UnicodeEncodeError: 'utf-8' codec can't encode character...
```

## 💡 Sugerir Mejoras

Para sugerir una mejora:

1. Abre un issue con el título "Enhancement: [descripción]"
2. Describe la mejora propuesta
3. Explica por qué sería útil
4. Proporciona ejemplos si es posible

### Ejemplo de sugerencia:

```
Título: Enhancement: Soporte para múltiples idiomas

Descripción:
Sería útil poder generar PDFs en diferentes idiomas.

Beneficios:
- Alcance global
- Mejor experiencia de usuario
- Más casos de uso

Ejemplo:
python generar_pdf_correos.py --language es
python generar_pdf_correos.py --language en
```

## 🔧 Contribuir Código

### Preparación

1. **Fork el repositorio**
   ```bash
   git clone https://github.com/tu-usuario/email-to-pdf-generator.git
   cd email-to-pdf-generator
   ```

2. **Crear una rama**
   ```bash
   git checkout -b feature/mi-mejora
   # o
   git checkout -b fix/mi-bug
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

### Desarrollo

1. **Hacer cambios** en tu rama
2. **Ejecutar pruebas**
   ```bash
   python test_generator.py
   ```

3. **Verificar código**
   ```bash
   make lint      # Si está disponible
   make format    # Si está disponible
   ```

### Commit

Usa mensajes de commit claros y descriptivos:

```bash
git commit -m "Fix: Corregir error de codificación UTF-8"
git commit -m "Feature: Agregar soporte para múltiples idiomas"
git commit -m "Docs: Actualizar README con ejemplos"
git commit -m "Refactor: Simplificar lógica de generación de PDF"
```

### Formato de Mensajes de Commit

```
<tipo>: <descripción corta>

<descripción detallada si es necesario>

Fixes #123
```

Tipos válidos:
- `Feature`: Nueva funcionalidad
- `Fix`: Corrección de bug
- `Docs`: Cambios en documentación
- `Refactor`: Cambios en código sin alterar funcionalidad
- `Test`: Agregar o actualizar pruebas
- `Chore`: Cambios en configuración, dependencias, etc.

### Push y Pull Request

1. **Push a tu fork**
   ```bash
   git push origin feature/mi-mejora
   ```

2. **Crear Pull Request**
   - Ve a GitHub
   - Haz clic en "New Pull Request"
   - Selecciona tu rama
   - Completa la descripción

3. **Descripción del PR**
   ```markdown
   ## Descripción
   Breve descripción de los cambios

   ## Tipo de cambio
   - [ ] Bug fix
   - [ ] Nueva funcionalidad
   - [ ] Cambio que rompe compatibilidad

   ## Cómo se probó
   Describe cómo probaste los cambios

   ## Checklist
   - [ ] Mi código sigue el estilo del proyecto
   - [ ] He ejecutado las pruebas localmente
   - [ ] He actualizado la documentación
   - [ ] No hay cambios sin documentar
   ```

## 📝 Estilo de Código

### Python

- Usa **PEP 8** como guía
- Máximo 100 caracteres por línea
- Usa nombres descriptivos para variables y funciones
- Agrega docstrings a funciones y clases

```python
def generate_pdf(emails, output_file='correos.pdf'):
    """
    Genera un PDF a partir de una lista de correos.
    
    Args:
        emails (list): Lista de diccionarios con correos
        output_file (str): Ruta del archivo PDF de salida
        
    Returns:
        bool: True si se generó exitosamente, False en caso contrario
    """
    # Implementación
    pass
```

### HTML/CSS

- Indentación de 4 espacios
- Nombres de clases en kebab-case
- Comentarios descriptivos

```html
<!-- Encabezado del correo -->
<div class="email-header">
    <h2 class="email-subject">{{ email.subject }}</h2>
</div>
```

## 📚 Documentación

Si agregas una nueva funcionalidad:

1. **Actualiza README.md** si es necesario
2. **Agrega ejemplos** en GUIA_AVANZADA.md
3. **Documenta parámetros** en docstrings
4. **Actualiza PROYECTO_RESUMEN.md**

## 🧪 Testing

Antes de hacer un PR:

1. **Ejecuta las pruebas**
   ```bash
   python test_generator.py
   ```

2. **Prueba manualmente**
   ```bash
   python generar_pdf_correos.py
   python generar_pdf_desde_json.py ejemplo_correos.json
   ```

3. **Agrega pruebas** para nuevas funcionalidades

## 📦 Dependencias

Si necesitas agregar una dependencia:

1. Actualiza `requirements.txt`
2. Justifica por qué es necesaria
3. Menciona en el PR

## 🔄 Proceso de Revisión

1. Un mantenedor revisará tu PR
2. Puede solicitar cambios
3. Una vez aprobado, se fusionará

## 📖 Recursos

- [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)
- [Git Workflow](https://git-scm.com/book/en/v2)
- [Markdown Guide](https://www.markdownguide.org/)

## ❓ Preguntas

Si tienes preguntas:

1. Revisa la documentación existente
2. Abre un issue con la etiqueta "question"
3. Contacta a los mantenedores

## 🎉 ¡Gracias!

Tu contribución es valiosa y apreciada. Juntos hacemos este proyecto mejor.

---

**Última actualización:** 2026-09-26
