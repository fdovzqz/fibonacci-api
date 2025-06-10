from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/echo', methods=['POST'])
def echo():
    """
    Endpoint echo que devuelve en formato JSON lo que recibe
    """
    try:
        # Obtener datos del request
        if request.is_json:
            # Si es JSON, devolver directamente
            data = request.get_json()
        else:
            # Si no es JSON, obtener datos como form data o raw
            data = request.get_data(as_text=True)
            if not data:
                data = dict(request.form)
        
        # Crear respuesta
        response = data
        return jsonify(response), 200
    
    except Exception as e:
        error_response = {
            "status": "error",
            "message": str(e),
            "data": None
        }
        return jsonify(error_response), 500

@app.route('/health', methods=['GET'])
def health():
    """
    Endpoint de salud para verificar que la aplicación está funcionando
    """
    return jsonify({
        "status": "healthy",
        "message": "Echo service is running"
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False) 