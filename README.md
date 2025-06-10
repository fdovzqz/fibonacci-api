# Echo API - AWS App Runner Deployment

API simple de echo que devuelve en formato JSON lo que recibe. Configurada para desplegar en AWS App Runner usando CDK.

## Estructura del Proyecto

```
/
├── app/                # Código fuente de la app (contenedor)
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── test-local.sh
│   ├── apprunner.yaml
│   └── .env.example
│
├── infra/              # Infraestructura CDK
│   ├── package.json
│   ├── pnpm-lock.yaml
│   ├── tsconfig.json
│   ├── cdk.json
│   ├── bin/
│   │   └── echo-api-cdk.ts
│   └── lib/
│       └── echo-api-cdk-stack.ts
│
├── .github/
│   └── workflows/
│       └── deploy.yml
│
├── README.md
└── .gitignore
```

## Características

- API Flask simple con endpoints `/echo` y `/health`
- Deployment automatizado en AWS App Runner
- Configuración de CDK para infraestructura como código
- GitHub Actions para CI/CD

## Endpoints

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

## Deployment en AWS

### Prerrequisitos

1. **AWS CLI configurado** con credenciales apropiadas
2. **Node.js 18+** instalado
3. **pnpm** instalado: `npm install -g pnpm`
4. **CDK CLI** instalado globalmente: `pnpm add -g aws-cdk`
5. **Repositorio en GitHub** con el código

### Configuración Inicial

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/TU_USUARIO/echo-api.git
   cd echo-api
   ```

2. **Instalar dependencias de infraestructura:**
   ```bash
   cd infra
   pnpm install
   ```

3. **Configurar el repositorio de GitHub:**
   Editar `infra/lib/echo-api-cdk-stack.ts` y cambiar la URL del repositorio:
   ```typescript
   repositoryUrl: 'https://github.com/TU_USUARIO/echo-api', // Cambiar por tu repositorio
   ```

4. **Configurar GitHub Secrets:**
   En tu repositorio de GitHub, ir a Settings > Secrets and variables > Actions y agregar:
   - `AWS_ACCESS_KEY_ID`: Tu AWS Access Key ID
   - `AWS_SECRET_ACCESS_KEY`: Tu AWS Secret Access Key

### Deployment Automático

El deployment se ejecuta automáticamente cuando se hace push a la rama `main`.

### Deployment Manual

1. **Bootstrap CDK (solo la primera vez):**
   ```bash
   cd infra
   pnpm cdk bootstrap
   ```

2. **Deploy:**
   ```bash
   cd infra
   pnpm cdk deploy
   ```

### Comandos Útiles

- **Ver diferencias:**
  ```bash
  cd infra
  pnpm cdk diff
  ```
- **Destruir stack:**
  ```bash
  cd infra
  pnpm cdk destroy
  ```

## Configuración de App Runner

El servicio se configura con:
- **Runtime:** Python 3.11
- **CPU:** 1 vCPU
- **Memoria:** 2 GB
- **Puerto:** 5000
- **Auto-deployment:** Habilitado

## Desarrollo Local

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

## Docker

También puedes ejecutar la aplicación usando Docker:

```bash
cd app
docker build -t echo-api .
docker run -p 5000:5000 echo-api
``` 