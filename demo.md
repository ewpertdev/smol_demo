# DEMO: Sistema Simple de Control de Gastos

## 1. VERSIÓN ACTUAL
Sistema web básico que permite a usuarios registrar y hacer seguimiento de sus gastos personales.

## 2. TECNOLOGÍAS IMPLEMENTADAS VS PLANEADAS

### 2.1 BACKEND
#### Planeado:
- Python con Flask para APIs RESTful completas
- Despliegue en Heroku
- Integración con servicios OCR

#### Implementado:
- Python 3.10
- Flask 2.0.1
- SQLAlchemy 1.4.23
- Flask-SQLAlchemy 2.5.1
- Despliegue local

### 2.2 FRONTEND
#### Planeado:
- Flutter (aplicación móvil)
- Widgets personalizados
- Multiplataforma (iOS/Android)

#### Implementado:
- HTML5
- CSS básico
- JavaScript vanilla
- Diseño web responsive simple

### 2.3 BASE DE DATOS
#### Planeado:
- MySQL con múltiples tablas
- Grupos de usuarios
- Gastos compartidos
- Categorías

#### Implementado:
- MySQL 8.0
- PyMySQL 1.0.2
- Solo tablas esenciales (users, expenses)

### 2.4 CARACTERÍSTICAS NO IMPLEMENTADAS
- OCR para escaneo de facturas
- Grupos de gastos compartidos
- Sincronización en tiempo real
- Notificaciones
- Gráficos de balance
- Integración con sistemas de pago

## 3. FUNCIONALIDADES IMPLEMENTADAS

### 3.1 Gestión de Usuarios
- Registro de nuevos usuarios
- Login con email y contraseña
- Logout
- Sesiones de usuario

### 3.2 Gestión de Gastos
- Añadir nuevos gastos
- Ver lista de gastos personal
- Calcular total de gastos
- Datos separados por usuario

## 4. ESTRUCTURA DE DATOS

### 4.1 Tabla Users
- `id` (PRIMARY KEY)
- `email` (UNIQUE)
- `password_hash`
- `username`

### 4.2 Tabla Expenses
- `id` (PRIMARY KEY)
- `description`
- `amount`
- `user_id` (FOREIGN KEY)
- `created_at`

## 5. ARCHIVOS DEL PROYECTO

### 5.1 Backend
- `app.py` (aplicación principal)
- `schema.sql` (estructura de base de datos)
- `requirements.txt` (dependencias)

### 5.2 Frontend
```
templates/
├── index.html (página principal)
└── login.html (registro/login)
```

## 6. GUÍAS DE INSTALACIÓN
- `instalarpython.md` (instalación de Python)
- `instalararchivos.md` (configuración del proyecto)
- `README.md` (documentación general)

## 7. EQUIPO
- Jairo Acosta Condor
- Mohd Firdaus Bin Abdullah

## 8. NOTAS SOBRE LA DEMO
- Esta versión es una prueba de concepto
- Demuestra la funcionalidad core del sistema
- Base para futuras implementaciones
- Enfoque en estabilidad y simplicidad 