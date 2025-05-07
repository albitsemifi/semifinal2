import os
from flask import Flask, jsonify, render_template_string, request

app = Flask(__name__)

@app.route('/')
def home():
    if 'application/json' in request.headers.get('Accept', ''):
        return jsonify({
            "app": "Flask API",
            "status": "running",
            "version": "1.0"
        })

    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Welcome</title>
    </head>
    <body>
        <h1>Flask API</h1>
        <p>A simple web service</p>
    </body>
    </html>
    ''')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
