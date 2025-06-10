# Echo API - AWS App Runner Deployment

API simple de echo que devuelve en formato JSON lo que recibe. Configurada para desplegar en AWS App Runner usando GitHub Actions y AWS CLI.

## 🚀 Estado del Proyecto

✅ **Listo para deployment** - Configuración completa para AWS App Runner con AWS CLI

## 📁 Estructura del Proyecto

```
/
├── app/                # Código fuente de la app (contenedor)
│   ├── app.py          # Aplicación Flask
│   ├── requirements.txt # Dependencias Python
│   ├── Dockerfile      # Configuración Docker
│   ├── test-local.sh   # Script de pruebas locales
│   ├── apprunner.yaml  # Configuración App Runner
│   └── .env.example    # Variables de entorno de ejemplo
│
├── .github/
│   └── workflows/
│       └── deploy.yml  # CI/CD con GitHub Actions
│
├── README.md
└── .gitignore
```

## 🔧 Tecnologías Utilizadas

- **Backend:** Flask (Python 3.11)
- **Deployment:** AWS App Runner
- **CI/CD:** GitHub Actions + AWS CLI
- **Container:** Docker

## 🌐 Endpoints

### POST /echo
Devuelve en formato JSON los datos recibidos en el request.

**Ejemplo:**
```bash
curl -X POST https://tu-app-runner-url/echo \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello World"}'
```

**Respuesta:**
```json
{
  "message": "Hello World"
}
```

### GET /health
Endpoint de salud para verificar que la aplicación está funcionando.

**Ejemplo:**
```bash
curl https://tu-app-runner-url/health
```

**Respuesta:**
```json
{
  "status": "healthy",
  "message": "Echo service is running"
}
```

## 🚀 Deployment en AWS (Automatizado)

### Prerrequisitos

1. **AWS CLI configurado** con credenciales apropiadas
2. **Repositorio en GitHub** con el código
3. **Configurar GitHub Secrets:**
   - `AWS_ACCESS_KEY_ID`: Tu AWS Access Key ID
   - `AWS_SECRET_ACCESS_KEY`: Tu AWS Secret Access Key

### Deployment Automático

El deployment se ejecuta automáticamente cuando se hace push a la rama `main` gracias al workflow de GitHub Actions. El workflow utiliza AWS CLI para crear o actualizar el servicio en App Runner.

### Workflow relevante (`.github/workflows/deploy.yml`):

```yaml
- name: Create App Runner Service
  run: |
    aws apprunner create-service \
      --service-name echo-api-service \
      --source-configuration '{
        "AutoDeploymentsEnabled": true,
        "CodeRepository": {
          "CodeConfiguration": {
            "ConfigurationSource": "REPOSITORY"
          },
          "RepositoryUrl": "https://github.com/fdovzqz/echo-docker.git",
          "SourceCodeVersion": {
            "Type": "BRANCH",
            "Value": "main"
          }
        }
      }' \
      --instance-configuration '{
        "Cpu": "1 vCPU",
        "Memory": "2 GB"
      }' \
      --region us-east-1 || echo "Service may already exist"

- name: Get Service URL
  run: |
    SERVICE_URL=$(aws apprunner describe-service --service-name echo-api-service --region us-east-1 --query 'Service.ServiceUrl' --output text)
    echo "App Runner Service URL: $SERVICE_URL"
```

## 🧪 Desarrollo Local

1. **Configurar variables de entorno (opcional):**
   ```bash
   cd app
   cp .env.example .env
   # Editar .env según sea necesario
   ```

2. **Instalar dependencias:**
   ```bash
   cd app
   pip3 install -r requirements.txt
   ```

3. **Ejecutar aplicación:**
   ```bash
   cd app
   python3 app.py
   ```

4. **Probar endpoints:**
   ```bash
   curl -X POST http://localhost:5000/echo \
     -H "Content-Type: application/json" \
     -d '{"test": "data"}'
   
   curl http://localhost:5000/health
   ```

5. **Probar todo con script:**
   ```bash
   cd app
   ./test-local.sh
   ```

## 🐳 Docker

También puedes ejecutar la aplicación usando Docker:

```bash
cd app
docker build -t echo-api .
docker run -p 5000:5000 echo-api
```

## 📊 Monitoreo

Una vez desplegado, podrás:
- Ver logs en CloudWatch Logs
- Acceder a métricas automáticas de App Runner
- Recibir la URL del servicio en los outputs del workflow

## 🔧 Troubleshooting

- **Error de credenciales:** Verifica que los GitHub Secrets estén configurados
- **Error de bucket S3:** Si usaste CDK antes, asegúrate de borrar los buckets y stacks antiguos
- **Logs útiles:**
  - **GitHub Actions:** Revisa la pestaña Actions en tu repo
  - **AWS App Runner:** Consola de AWS > App Runner > Tu servicio > Logs

## 🤝 Contribución

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request 