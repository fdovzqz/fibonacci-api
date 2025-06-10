# Fibonacci API

Una API REST simple que calcula números de la secuencia de Fibonacci, desplegada en AWS App Runner.

## 🚀 Características

- **Endpoint principal**: `/fibonacci/<position>` - Calcula el número de Fibonacci en la posición especificada
- **Health check**: `/health` - Verifica el estado del servicio
- **Despliegue**: Configurado para AWS App Runner con Docker
- **Escalabilidad**: Automáticamente escalable según la demanda

## 📋 Prerrequisitos

- Cuenta de AWS con permisos para App Runner
- Docker instalado (para pruebas locales)
- Python 3.11+ (para desarrollo local)

## 🏗️ Estructura del Proyecto

```
fibonacci-api/
├── app.py              # Aplicación Flask principal
├── requirements.txt    # Dependencias de Python
├── Dockerfile         # Configuración de Docker
├── apprunner.yaml     # Configuración de AWS App Runner
└── README.md          # Este archivo
```

## 🐳 Ejecución Local con Docker

```bash
# Construir la imagen
docker build -t fibonacci-api .

# Ejecutar el contenedor
docker run -p 8000:8000 fibonacci-api

# Probar la API
curl http://localhost:8000/fibonacci/10
curl http://localhost:8000/health
```

## 🚀 Deployment Manual a AWS App Runner

### Paso 1: Preparar el Repositorio

1. **Asegúrate de que el código esté en GitHub**:
   ```bash
   git add .
   git commit -m "Preparar para deployment a App Runner"
   git push origin main
   ```

2. **Verifica que los archivos estén en el repositorio**:
   - `app.py`
   - `requirements.txt`
   - `Dockerfile`
   - `apprunner.yaml`

### Paso 2: Crear el Servicio en AWS App Runner

1. **Accede a AWS Console**:
   - Ve a [AWS App Runner Console](https://console.aws.amazon.com/apprunner/)
   - Selecciona tu región preferida

2. **Crear nuevo servicio**:
   - Haz clic en "Create service"
   - Selecciona "Source code repository"
   - Conecta tu cuenta de GitHub (si no lo has hecho antes)

3. **Configurar el repositorio**:
   - Selecciona tu repositorio `fibonacci-api`
   - Selecciona la rama `main`
   - En "Deployment trigger", elige "Automatic" para deployments automáticos

4. **Configurar el build**:
   - **Build type**: `Dockerfile`
   - **Dockerfile path**: `Dockerfile` (dejar por defecto)
   - **Port**: `8000`

5. **Configurar el servicio**:
   - **Service name**: `fibonacci-api` (o el nombre que prefieras)
   - **CPU**: `1 vCPU` (suficiente para empezar)
   - **Memory**: `2 GB` (recomendado)
   - **Environment variables**: No necesarias por ahora

6. **Configurar el acceso**:
   - **Public endpoint**: Habilitado (para acceso público)
   - **VPC**: Por defecto (si no necesitas VPC específica)

### Paso 3: Desplegar y Verificar

1. **Revisar y crear**:
   - Revisa la configuración
   - Haz clic en "Create & deploy"

2. **Monitorear el deployment**:
   - El proceso tomará 5-10 minutos
   - Puedes ver los logs en tiempo real

3. **Obtener la URL del servicio**:
   - Una vez completado, App Runner te dará una URL como:
   - `https://xxxxxxxxxx.us-east-1.awsapprunner.com`

### Paso 4: Probar la API

```bash
# Probar el endpoint de Fibonacci
curl https://tu-url-apprunner.awsapprunner.com/fibonacci/10

# Probar el health check
curl https://tu-url-apprunner.awsapprunner.com/health
```

## 📚 Documentación de la API

### Endpoints

#### GET `/fibonacci/<position>`
Calcula el número de Fibonacci en la posición especificada.

**Parámetros**:
- `position` (integer): Posición en la secuencia (debe ser ≥ 0)

**Respuesta exitosa** (200):
```json
{
  "position": 10,
  "value": 55
}
```

**Respuesta de error** (400):
```json
{
  "error": "Position must be non-negative"
}
```

#### GET `/health`
Verifica el estado del servicio.

**Respuesta** (200):
```json
{
  "status": "healthy"
}
```

### Ejemplos de Uso

```bash
# Obtener el 10º número de Fibonacci
curl https://tu-url-apprunner.awsapprunner.com/fibonacci/10

# Obtener el 20º número de Fibonacci
curl https://tu-url-apprunner.awsapprunner.com/fibonacci/20

# Verificar el estado del servicio
curl https://tu-url-apprunner.awsapprunner.com/health
```

## 🔧 Configuración Avanzada

### Variables de Entorno
Puedes agregar variables de entorno en la configuración de App Runner:
- `PORT`: Puerto del servicio (por defecto 8000)
- `FLASK_ENV`: Entorno de Flask (development/production)

### Escalado Automático
App Runner maneja automáticamente el escalado basado en:
- Número de requests concurrentes
- Uso de CPU
- Uso de memoria

### Monitoreo
- **CloudWatch Logs**: Automáticamente habilitados
- **Métricas**: CPU, memoria, requests por segundo
- **Trazas**: X-Ray disponible para debugging

## 🛠️ Desarrollo Local

```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar en modo desarrollo
python app.py

# Ejecutar con gunicorn (producción)
gunicorn --bind 0.0.0.0:8000 app:app
```

## 📝 Notas Importantes

- **Límites**: Para números muy grandes (> 1000), la función puede ser lenta
- **Memoria**: La implementación actual es iterativa, eficiente en memoria
- **Seguridad**: El endpoint es público, considera agregar autenticación si es necesario
- **Costos**: App Runner cobra por vCPU y memoria utilizados

## 🔄 Actualizaciones

Para actualizar el servicio:
1. Haz cambios en tu código
2. Haz commit y push a GitHub
3. App Runner detectará automáticamente los cambios y hará un nuevo deployment

## 🆘 Troubleshooting

### Problemas Comunes

1. **Build falla**:
   - Verifica que `requirements.txt` esté correcto
   - Revisa los logs de build en App Runner

2. **Aplicación no responde**:
   - Verifica que el puerto 8000 esté configurado correctamente
   - Revisa los logs de la aplicación

3. **Errores de memoria**:
   - Aumenta la memoria asignada en la configuración de App Runner

### Logs y Debugging

- Los logs están disponibles en CloudWatch
- Puedes ver logs en tiempo real durante el deployment
- Usa el endpoint `/health` para verificar el estado del servicio

