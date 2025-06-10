# Fibonacci API

API REST simple que calcula números de la secuencia de Fibonacci, desplegada en AWS App Runner.

## 🚀 Características

- **Endpoint principal**: `/fibonacci/<position>` - Calcula el número de Fibonacci en la posición especificada
- **Health check**: `/health` - Verifica el estado del servicio
- **Despliegue**: Configurado para AWS App Runner
- **Escalabilidad**: Automáticamente escalable según la demanda

## 📋 Estructura del Proyecto

```
fibonacci-api/
├── app.py              # Aplicación Flask principal
├── requirements.txt    # Dependencias de Python
├── Dockerfile         # Configuración de Docker
├── apprunner.yaml     # Configuración de AWS App Runner
└── README.md          # Este archivo
```

## 🐳 Ejecución Local

```bash
# Con Docker
docker build -t fibonacci-api .
docker run -p 8000:8000 fibonacci-api

# Con Python
pip install -r requirements.txt
python app.py
```

## 📚 API Endpoints

### GET `/fibonacci/<position>`
Calcula el número de Fibonacci en la posición especificada.

**Ejemplo**:
```bash
curl https://tu-url-apprunner.awsapprunner.com/fibonacci/10
```

**Respuesta**:
```json
{
  "position": 10,
  "value": 55
}
```

### GET `/health`
Verifica el estado del servicio.

**Ejemplo**:
```bash
curl https://tu-url-apprunner.awsapprunner.com/health
```

**Respuesta**:
```json
{
  "status": "healthy"
}
```

## 🚀 Deployment

El proyecto está configurado para deployment automático en AWS App Runner:

1. **Push a GitHub**: Los cambios en `main` activan deployment automático
2. **Configuración**: Usa `apprunner.yaml` para configuración específica
3. **Runtime**: Python 3.9 con Flask 2.2.5 y gunicorn 20.1.0

## 🛠️ Desarrollo

```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar en desarrollo
python app.py

# Ejecutar en producción
gunicorn --bind 0.0.0.0:8000 app:app
```