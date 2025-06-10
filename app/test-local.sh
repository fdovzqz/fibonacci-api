#!/bin/bash

echo "🚀 Probando la aplicación Echo API localmente..."

# Instalar dependencias
echo "📦 Instalando dependencias..."
pip3 install -r requirements.txt

# Ejecutar la aplicación en background
echo "🔧 Iniciando la aplicación..."
python3 app.py &
APP_PID=$!

# Esperar un momento para que la aplicación se inicie
sleep 3

# Probar el endpoint de salud
echo "🏥 Probando endpoint /health..."
curl -s http://localhost:5000/health | python3 -m json.tool

# Probar el endpoint echo
echo "🔄 Probando endpoint /echo..."
curl -s -X POST http://localhost:5000/echo \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello World", "test": true}' | python3 -m json.tool

# Detener la aplicación
echo "🛑 Deteniendo la aplicación..."
kill $APP_PID

echo "✅ Pruebas completadas!" 