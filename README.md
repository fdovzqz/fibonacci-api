# Fibonacci API

Una API REST simple que calcula números de la secuencia de Fibonacci, desplegada en AWS App Runner usando CDK.

## 🚀 Características

- **API REST**: Endpoint para calcular números de Fibonacci por posición
- **Health Check**: Endpoint de verificación de salud
- **Containerizado**: Aplicación Dockerizada para fácil despliegue
- **Infraestructura como Código**: Despliegue automatizado con AWS CDK
- **Escalabilidad**: Desplegado en AWS App Runner para escalabilidad automática

## 📋 Prerrequisitos

- Python 3.11+
- Docker
- AWS CLI configurado
- AWS CDK CLI
- Node.js (para CDK)

## 🏗️ Estructura del Proyecto

```
echo/
├── app.py                 # Aplicación Flask principal
├── requirements.txt       # Dependencias de Python
├── Dockerfile            # Configuración de Docker
├── apprunner.yaml        # Configuración de AWS App Runner
├── cdk/                  # Infraestructura como Código
│   ├── app.py           # Punto de entrada de CDK
│   ├── fibonacci_stack.py # Stack de AWS CDK
│   └── requirements.txt  # Dependencias de CDK
└── README.md            # Este archivo
```

## 🛠️ Instalación y Desarrollo Local

### 1. Clonar el repositorio
```bash
git clone <tu-repositorio>
cd echo
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3. Ejecutar localmente
```bash
python app.py
```

La aplicación estará disponible en `http://localhost:8000`

## 🐳 Ejecutar con Docker

### Construir la imagen
```bash
docker build -t fibonacci-api .
```

### Ejecutar el contenedor
```bash
docker run -p 8000:8000 fibonacci-api
```

## 📡 API Endpoints

### GET /fibonacci/{position}
Calcula el número de Fibonacci en la posición especificada.

**Parámetros:**
- `position` (integer): Posición en la secuencia (debe ser >= 0)

**Ejemplo de respuesta:**
```json
{
  "position": 10,
  "value": 55
}
```

**Ejemplo de error:**
```json
{
  "error": "Position must be non-negative"
}
```

### GET /health
Verifica el estado de salud de la aplicación.

**Ejemplo de respuesta:**
```json
{
  "status": "healthy"
}
```

## 🐳 Despliegue en AWS

### 1. Configurar CDK
```bash
cd cdk
pip install -r requirements.txt
cdk bootstrap
```

### 2. Actualizar configuración
Edita `cdk/fibonacci_stack.py` y actualiza:
- `repository_url`: URL de tu repositorio GitHub
- `service_name`: Nombre del servicio (opcional)

### 3. Desplegar
```bash
cdk deploy
```

### 4. Obtener la URL del servicio
```bash
aws apprunner list-services
```

## 🔧 Configuración

### Variables de Entorno
- `PORT`: Puerto en el que se ejecuta la aplicación (default: 8000)

### Configuración de App Runner
- **CPU**: 0.25 vCPU
- **Memoria**: 0.5 GB
- **Health Check**: `/health` cada 10 segundos
- **Auto-deploy**: Habilitado

## 🧪 Testing

### Probar endpoints localmente
```bash
# Health check
curl http://localhost:8000/health

# Fibonacci
curl http://localhost:8000/fibonacci/10
```

### Probar con Docker
```bash
# Health check
curl http://localhost:8000/health

# Fibonacci
curl http://localhost:8000/fibonacci/15
```

## 📊 Monitoreo

La aplicación incluye:
- Health check automático en `/health`
- Logs de aplicación disponibles en CloudWatch
- Métricas de App Runner en AWS Console

## 🔒 Seguridad

- La aplicación se ejecuta en un contenedor aislado
- IAM roles configurados para acceso mínimo necesario
- Health checks para detectar fallos

## 🚨 Limitaciones

- La función de Fibonacci es iterativa y puede ser lenta para números muy grandes
- No hay límite de entrada configurado (puede causar timeouts)
- Sin autenticación implementada

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.

## 📞 Soporte

Para soporte, por favor abrir un issue en el repositorio o contactar al equipo de desarrollo. 