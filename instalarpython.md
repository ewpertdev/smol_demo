# Guía de Instalación de Python en Windows

## 1. Descargar Python

1. **Ir a la página oficial**:
   - Abre el navegador
   - Ve a: https://www.python.org/downloads/
   - Click en "Download Python 3.10.x" (la última versión estable)

2. **Importante**: Descarga la versión de 64 bits si el sistema lo permite

## 2. Instalar Python

1. **Ejecutar el instalador**:
   - Busca el archivo descargado (normalmente en Descargas)
   - Nombre típico: `python-3.10.x-amd64.exe`
   - Haz doble clic

2. **En la primera pantalla**:
   - IMPORTANTE: Marca "Add Python 3.10 to PATH"
   - Click en "Install Now"
   - Si pide permisos de administrador, contacta al técnico del colegio

3. **Esperar** a que termine la instalación

## 3. Verificar la Instalación

1. **Abrir CMD** (Símbolo del sistema):
   - Presiona `Windows + R`
   - Escribe `cmd`
   - Presiona Enter

2. **Verificar Python**:
```bash
python --version
```
Deberías ver algo como: `Python 3.10.x`

3. **Verificar PIP** (el gestor de paquetes):
```bash
pip --version
```
Deberías ver algo como: `pip 22.x.x`

## 4. Posibles Problemas

### Si Python no se encuentra
1. **Verificar PATH**:
   - Busca "Variables de entorno" en Windows
   - En Variables del sistema, busca "Path"
   - Verifica que existe una entrada como:
     ```
     C:\Users\[usuario]\AppData\Local\Programs\Python\Python310\
     C:\Users\[usuario]\AppData\Local\Programs\Python\Python310\Scripts\
     ```

### Si necesitas permisos de administrador
1. Contacta al técnico del colegio
2. Necesitarás:
   - Permisos para instalar programas
   - Permisos para modificar PATH
   - Acceso a CMD

## 5. Verificación Final

1. **Probar Python**:
```bash
python
```
Deberías ver el intérprete de Python (>>>)
Para salir, escribe:
```python
exit()
```

2. **Probar un script simple**:
```bash
python -c "print('Hello, World!')"
```

## Notas Importantes

- Si ya hay Python instalado:
  1. Verifica la versión
  2. Asegúrate de que sea 3.8 o superior
  3. Verifica que pip esté disponible

## Próximos Pasos

Una vez instalado Python:
1. Sigue las instrucciones en `instalararchivos.md`
2. Configura el entorno virtual
3. Instala las dependencias del proyecto
