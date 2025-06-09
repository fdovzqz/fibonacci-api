# Echo Service con Flask

Un servicio simple de echo construido con Flask y Docker usando Alpine Linux.

## Características

- **Base**: Alpine Linux (imagen ligera)
- **Framework**: Flask
- **Endpoint**: POST `/echo` que devuelve en formato JSON lo que recibe
- **Health Check**: GET `/health` para verificar el estado del servicio

## Construir la imagen

```bash
docker build -t echo-service .
```

## Ejecutar el contenedor

```bash
docker run -p 5000:5000 echo-service
```

## Uso del endpoint echo

### Ejemplo con curl

```bash
# Enviar JSON
curl -X POST http://localhost:5000/echo \
  -H "Content-Type: application/json" \
  -d '{"message": "Hola mundo", "timestamp": "2024-01-01"}'

# Enviar datos de formulario
curl -X POST http://localhost:5000/echo \
  -d "message=Hola mundo" \
  -d "timestamp=2024-01-01"
```

### Respuesta esperada

```json
{
  "status": "success",
  "message": "Echo response",
  "data": {
    "message": "Hola mundo",
    "timestamp": "2024-01-01"
  },
  "method": "POST",
  "headers": {
    "Content-Type": "application/json",
    "Content-Length": "58",
    ...
  }
}
```

## Health Check

```bash
curl http://localhost:5000/health
```

Respuesta:
```json
{
  "status": "healthy",
  "message": "Echo service is running"
}
```

## Estructura del proyecto

```
.
├── dockerfile      # Configuración de Docker
├── requirements.txt # Dependencias de Python
├── app.py         # Aplicación Flask
└── README.md      # Este archivo
``` 