# Lumace LMS - Learning Management System

## 📚 Descripción del Proyecto

Lumace LMS es una plataforma de gestión de aprendizaje (Learning Management System) desarrollada en Django, diseñada para ofrecer una experiencia educativa completa y moderna. La plataforma permite la gestión de cursos, estudiantes, contenido educativo y pagos de manera integral.

### 🎯 Características Principales

- **Sistema de Autenticación Completo**: Registro, login, verificación por email y gestión de perfiles de usuario
- **Gestión de Cursos**: Creación, organización por categorías y niveles (principiante, intermedio, avanzado)
- **Sistema de Pagos**: Integración con Stripe para procesamiento seguro de pagos
- **Ofertas Especiales**: Acceso anticipado y membresías de patrocinio
- **Panel de Administración**: Gestión completa desde el admin de Django
- **Sistema de Notificaciones**: Envío de correos automáticos y recibos de compra
- **Arquitectura Escalable**: Preparada para despliegue con Docker y servicios en la nube

## 🏗️ Arquitectura del Sistema

### Apps Principales

1. **`base`** - Aplicación base con modelos comunes, autenticación personalizada y templates base
2. **`landing`** - Página de inicio y presentación de la plataforma
3. **`cursos`** - Gestión completa de cursos, categorías y estudiantes inscritos
4. **`ofertas`** - Sistema de ofertas especiales y promociones
5. **`pagos`** - Procesamiento de pagos con Stripe e historial de transacciones
6. **`personal`** - Gestión de usuarios personalizados
7. **`sponsors`** - Sistema de patrocinio de la plataforma
8. **`costos`** - Gestión de precios y costos de productos
9. **`clases`** - Módulo para clases individuales (en desarrollo)
10. **`biblioteca`** - Sistema de recursos educativos (en desarrollo)

### Modelos de Datos Principales

#### BaseModel
Modelo abstracto que proporciona:
- Campos de auditoría (fecha_creacion, fecha_modificacion)
- Control de usuarios (usuario_creacion, usuario_modificacion)
- Estado activo/inactivo

#### CursosModel
- Información del curso (nombre, descripción, presentación)
- Categorización y niveles
- Portadas y media
- Precios con soporte multicurrency
- Contador de estudiantes inscritos

#### AlumnosInscritosModel
- Relación many-to-many entre usuarios y cursos
- Fecha de inscripción
- Unicidad para evitar inscripciones duplicadas

## 🛠️ Stack Tecnológico

### Backend
- **Django 5.2.4** - Framework web principal
- **PostgreSQL** - Base de datos principal
- **Redis** - Cache y broker para Celery
- **Celery** - Tareas asíncronas (envío de emails, procesamiento de pagos)

### Frontend
- **Bootstrap 5** - Framework CSS
- **Font Awesome** - Iconografía
- **Django Templates** - Sistema de plantillas
- **Crispy Forms** - Renderizado mejorado de formularios

### Integraciones
- **Stripe** - Procesamiento de pagos
- **Gmail SMTP** - Envío de correos electrónicos
- **Django-Allauth** - Autenticación y autorización
- **Django-Money** - Manejo de monedas y precios

### Infraestructura
- **Docker & Docker Compose** - Containerización
- **Nginx** - Servidor web y proxy reverso
- **WhiteNoise** - Manejo de archivos estáticos
- **Cloudflare** - CDN y protección

## 🚀 Instalación y Configuración

### Prerrequisitos
- Docker y Docker Compose
- Git

### Configuración con Docker

1. **Clonar el repositorio**
```bash
git clone <repository-url>
cd lumace-lms
```

2. **Configurar variables de entorno**
Crear archivo `.env` con:
```env
POSTGRESQL=postgresql://user:password@db:5432/lms_db
EMAIL_HOST_USER=tu_email@gmail.com
EMAIL_HOST_PASSWORD=tu_app_password
STRIPE_LIVE_SECRET_KEY=sk_live_...
STRIPE_TEST_SECRET_KEY=sk_test_...
```

3. **Levantar los servicios**
```bash
docker-compose up -d
```

4. **Ejecutar migraciones**
```bash
docker-compose exec django python manage.py migrate
```

5. **Crear superusuario**
```bash
docker-compose exec django python manage.py createsuperuser
```

### Configuración de Desarrollo

Si prefieres trabajar sin Docker:

1. **Crear entorno virtual**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

2. **Instalar dependencias**
```bash
pip install -r dependencias.txt
```

3. **Configurar base de datos local**
```bash
python manage.py migrate
```

4. **Ejecutar servidor de desarrollo**
```bash
python manage.py runserver
```

## 📁 Estructura del Proyecto

```
lumace-lms/
├── .devcontainer/          # Configuración para VS Code Dev Containers
├── base/                   # App base con modelos comunes
├── cursos/                 # Gestión de cursos y categorías
├── landing/                # Página de inicio
├── ofertas/                # Sistema de ofertas
├── pagos/                  # Procesamiento de pagos
├── personal/               # Gestión de usuarios
├── sponsors/               # Sistema de patrocinio
├── costos/                 # Gestión de precios
├── lms/                    # Configuración principal de Django
├── templates/              # Templates globales
├── static/                 # Archivos estáticos
├── media/                  # Archivos subidos por usuarios
├── nginx/                  # Configuración de Nginx
├── docker-compose.yml      # Orquestación de contenedores
└── dependencias.txt        # Dependencias de Python
```

## 🎨 Características de la Interfaz

### Design System
- **Tema**: Moderno y minimalista
- **Colores**: Esquema de colores profesional con Bootstrap
- **Tipografía**: Font Awesome para iconos, Bootstrap para texto
- **Responsivo**: Compatible con dispositivos móviles y desktop

### Páginas Principales
- **Landing Page**: Presentación de cursos destacados y beneficios
- **Catálogo de Cursos**: Lista completa de cursos disponibles
- **Detalle de Curso**: Información completa con precios y descripción
- **Página de Lanzamiento**: Oferta especial de acceso anticipado
- **Panel de Usuario**: Configuración de perfil y historial

## 💳 Sistema de Pagos

### Integración con Stripe
- **Checkout Sessions**: Páginas de pago seguras hospedadas por Stripe
- **Webhooks**: Procesamiento automático de eventos de pago
- **Historial**: Registro completo de todas las transacciones
- **Recibos**: Envío automático de recibos por email

### Tipos de Productos
- **Acceso Anticipado**: Membresía especial con beneficios exclusivos
- **Patrocinio**: Sistema de apoyo a la plataforma
- **Cursos**: Compra individual de cursos (en desarrollo)

## 🔧 Administración

### Panel de Admin Personalizado
- **Gestión de Usuarios**: CRUD completo con filtros avanzados
- **Gestión de Cursos**: Creación y edición con preview de contenido
- **Historial de Pagos**: Monitoreo de transacciones
- **Sistema de Auditoría**: Tracking de cambios y usuarios responsables

### Fieldsets Organizados
- Información principal
- Detalles específicos
- Auditoría (colapsado por defecto)

## 📧 Sistema de Notificaciones

### Tareas Asíncronas con Celery
- **Recibos de Compra**: Envío automático post-pago
- **Confirmación de Registro**: Verificación por email
- **Notificaciones de Sistema**: Alerts importantes

### Templates de Email
- Formato HTML con Markdown
- Diseño responsive
- Información completa de transacciones

## 🔒 Seguridad

### Autenticación
- Verificación obligatoria por email
- Integración con Django-Allauth
- Formularios personalizados con Crispy Forms

### Protección de Datos
- CSRF protection habilitado
- Validación de formularios
- Sanitización de contenido

## 🚀 Despliegue

### Configuración de Producción
- **Debug**: Desactivado
- **HTTPS**: Configurado para Cloudflare
- **Static Files**: Servidos por WhiteNoise
- **Database**: PostgreSQL en producción

### Docker Compose Services
```yaml
services:
  - django: Aplicación principal
  - db: PostgreSQL
  - redis: Cache y message broker
  - nginx: Servidor web
  - celery: Worker para tareas asíncronas
```

## 🎯 Roadmap

### Funcionalidades en Desarrollo
- **Sistema de Clases**: Clases individuales en vivo
- **Biblioteca Digital**: Recursos descargables
- **BiliBot**: Asistente AI para estudiantes
- **Certificaciones**: Emisión de certificados
- **Foro de Estudiantes**: Comunidad de aprendizaje

### Mejoras Técnicas
- API REST con Django Rest Framework
- Aplicación móvil
- Sistema de analytics avanzado
- Integración con plataformas de video

## 📄 Licencia

Este proyecto está desarrollado como una plataforma educativa comercial. Para más información sobre el uso y licenciamiento, contacta al equipo de desarrollo.


---

**Lumace LMS** - Transformando la educación en línea, un curso a la vez. 🚀