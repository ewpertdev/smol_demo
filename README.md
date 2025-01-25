# Control de Gastos - Demo

Una aplicación web simple para gestionar gastos personales, desarrollada con Flask y MySQL.

## Características
- 👤 Sistema de registro y login de usuarios
- 💰 Añadir gastos con descripción y monto
- 📊 Ver lista de gastos personales
- 💵 Calcular total de gastos
- 🔒 Datos separados por usuario

## Conceptos Técnicos Importantes

### ¿Qué es un Entorno Virtual?
Un entorno virtual (venv) es un espacio aislado donde instalamos las dependencias específicas de nuestro proyecto. Es fundamental porque:

1. **Aislamiento**: 
   - Cada proyecto puede tener sus propias versiones de bibliotecas
   - Evita conflictos entre diferentes proyectos
   - Ejemplo: Un proyecto puede usar Flask 1.0 y otro Flask 2.0 sin problemas

2. **Reproducibilidad**: 
   - El archivo `requirements.txt` lista las versiones exactas necesarias
   - Cualquier desarrollador puede recrear el mismo entorno
   - Garantiza que el proyecto funcione igual en cualquier máquina

3. **Limpieza**: 
   - Las dependencias se instalan solo para este proyecto
   - No afecta al Python global del sistema
   - Fácil de limpiar: solo hay que borrar la carpeta venv

4. **Portabilidad**: 
   - El proyecto no depende de bibliotecas globales
   - Facilita la colaboración entre desarrolladores
   - Ideal para demostraciones y presentaciones

## Requisitos Previos
1. Python 3.8 o superior
2. MySQL Server
3. Git (opcional)

## Instalación

1. **Clonar/Descargar el repositorio**
```bash
git clone <url-del-repositorio>
# o descargar y descomprimir el ZIP
```

2. **Crear un entorno virtual**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

4. **Configurar la base de datos**
- Abrir MySQL Workbench
- Conectar a localhost
- Ejecutar el siguiente script:
```sql
CREATE DATABASE gastos_demo;
USE gastos_demo;

CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    username VARCHAR(100) NOT NULL
);

CREATE TABLE expenses (
    id INT PRIMARY KEY AUTO_INCREMENT,
    description VARCHAR(255) NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    user_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

5. **Configurar la aplicación**
- Modificar en `app.py` la conexión a la base de datos si es necesario:
```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:tu_password@localhost/gastos_demo'
```

6. **Ejecutar la aplicación**
```bash
python app.py
```

7. **Acceder a la aplicación**
- Abrir navegador
- Ir a: http://localhost:5000

## Estructura del Proyecto
```
gastos_demo/
│
├── app.py              # Aplicación principal
├── requirements.txt    # Dependencias
├── schema.sql         # Esquema de la base de datos
│
└── templates/
    ├── index.html     # Página principal
    └── login.html     # Página de login/registro
```

## Tecnologías Utilizadas
- **Backend**: Flask (Python)
- **Base de Datos**: MySQL
- **ORM**: SQLAlchemy
- **Frontend**: HTML, CSS, JavaScript
- **Autenticación**: Flask-Session

## Funcionalidades Implementadas

### 1. Gestión de Usuarios
- Registro de nuevos usuarios
- Login con email y contraseña
- Sesiones de usuario
- Logout

### 2. Gestión de Gastos
- Añadir nuevos gastos
- Ver lista de gastos personal
- Calcular total de gastos
- Protección de datos por usuario

## Uso de la Aplicación

1. **Registro de Usuario**
   - Acceder a la página principal
   - Rellenar el formulario de registro
   - Usar email único y contraseña

2. **Login**
   - Ingresar email y contraseña
   - Acceder a dashboard personal

3. **Añadir Gastos**
   - Escribir descripción del gasto
   - Ingresar monto
   - Hacer clic en "Añadir"

4. **Ver Gastos**
   - Los gastos se muestran en la página principal
   - Se muestra el total actualizado

## Notas para el Desarrollo
- La aplicación usa `pymysql` para la conexión a MySQL
- Las contraseñas se almacenan hasheadas
- Incluye manejo básico de errores
- Diseño responsive simple

## Próximas Mejoras Posibles
- [ ] Categorías de gastos
- [ ] Filtros y búsqueda
- [ ] Gráficos y estadísticas
- [ ] Exportar datos
- [ ] Mejoras en la interfaz

## Equipo

- Jairo Acosta Condor
- Mohd Firdaus Bin Abdullah

