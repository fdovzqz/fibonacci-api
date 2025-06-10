from flask import Flask, jsonify, request

app = Flask(__name__)

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

@app.route('/fibonacci/<int:position>')
def get_fibonacci(position):
    if position < 0:
        return jsonify({'error': 'Position must be non-negative'}), 400
    
    result = fibonacci(position)
    return jsonify({
        'position': position,
        'value': result
    })

@app.route('/health')
def health_check():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)