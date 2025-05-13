# Interview Transcription Application - Código Fuente

## Estructura del Proyecto

La aplicación está organizada en una estructura modular y escalable:

/
├── app/
│   ├── api/
│   │   └── routes/
│   ├── core/
│   │   └── config/
│   ├── models/
│   └── services/
├── static/
│   ├── css/
│   └── js/
├── templates/
├── .env
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── main.py
└── requirements.txt

## Componentes Principales

### 1. API Routes (`app/api/routes/`)
- Maneja las rutas y endpoints de la API
- Procesa las solicitudes HTTP
- Gestiona la lógica de enrutamiento

### 2. Core Configuration (`app/core/config/`)
- Configuraciones centrales de la aplicación
- Variables de entorno
- Configuraciones de servicios

### 3. Models (`app/models/`)
- Definiciones de modelos de datos
- Esquemas de validación
- Estructuras de datos

### 4. Services (`app/services/`)
- Lógica de negocio principal
- Servicios de transcripción
- Procesamiento de audio

### 5. Static Files (`static/`)
- Archivos CSS para estilos
- JavaScript para funcionalidad del cliente
- Recursos estáticos

### 6. Templates (`templates/`)
- Plantillas HTML
- Vistas de la aplicación
- Componentes de interfaz

## Funcionalidad Principal

1. **Carga de Archivos**
   - Soporte para archivos de audio
   - Validación de formatos
   - Almacenamiento temporal

2. **Procesamiento de Audio**
   - Conversión de formatos
   - Optimización de audio
   - Preparación para transcripción

3. **Transcripción**
   - Integración con servicios de transcripción
   - Procesamiento de texto
   - Generación de resultados

4. **Interfaz de Usuario**
   - Diseño responsivo
   - Feedback en tiempo real
   - Experiencia de usuario intuitiva

## Dependencias

- Python 3.8+
- FastAPI
- SQLAlchemy
- PyDantic
- FFmpeg
- Docker/
├── app/
│   ├── api/
│   │   └── routes/
│   ├── core/
│   │   └── config/
│   ├── models/
│   └── services/
├── static/
│   ├── css/
│   └── js/
├── templates/
├── .env
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── main.py
└── requirements.txt