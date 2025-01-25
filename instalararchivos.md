# Guía de Instalación y Ejecución

## 1. Preparar el Entorno

### Navegar a la carpeta del proyecto
```bash
# Si estás en C:\WINDOWS\system32>
E:
cd "Trabajo TFG Bea"
```

### Crear y activar entorno virtual
```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
venv\Scripts\activate
```

## 2. Instalar Dependencias

### Instalar paquetes necesarios
```bash
# Instalar todas las dependencias del requirements.txt
pip install -r requirements.txt

# Si hay errores, instalar uno por uno:
pip install Flask==2.0.1
pip install SQLAlchemy==1.4.23
pip install Flask-SQLAlchemy==2.5.1
pip install PyMySQL==1.0.2
pip install python-dotenv==0.19.0
```

## 3. Configurar Base de Datos

1. Abrir MySQL Workbench
2. Conectar a localhost (usuario: root, contraseña: fir)
3. Ejecutar los comandos del archivo schema.sql:
```sql
CREATE DATABASE gastos_demo;
USE gastos_demo;

-- Copiar y pegar el contenido de schema.sql
```

## 4. Ejecutar la Aplicación

```bash
# Asegurarse de estar en el entorno virtual (debe verse (venv) al inicio)
python app.py
```

## 5. Acceder a la Aplicación

1. Abrir navegador
2. Ir a: http://localhost:5000

## Solución de Problemas Comunes

### Error: "No module named 'MySQLdb'"
```bash
pip install mysqlclient
```

### Error: "Cannot connect to MySQL"
- Verificar que MySQL está corriendo
- Verificar credenciales en app.py:
```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:fir@localhost/gastos_demo'
```

### Error: "Table already exists"
```sql
-- En MySQL Workbench:
DROP DATABASE IF EXISTS gastos_demo;
CREATE DATABASE gastos_demo;
```

### Error: "No module named flask_sqlalchemy"
```bash
pip uninstall flask flask-sqlalchemy sqlalchemy
pip install Flask==2.0.1
pip install SQLAlchemy==1.4.23
pip install Flask-SQLAlchemy==2.5.1
```

## Estructura de Archivos Necesaria
```
E:\Trabajo TFG Bea\
    ├── app.py
    ├── requirements.txt
    ├── schema.sql
    └── templates\
        ├── index.html
        └── login.html
```

## Verificación de Instalación

Para verificar que todo está instalado correctamente:
```bash
pip list
```

Deberías ver:
- Flask==2.0.1
- Flask-SQLAlchemy==2.5.1
- SQLAlchemy==1.4.23
- PyMySQL==1.0.2
- Werkzeug==2.0.1
- (y otras dependencias)
