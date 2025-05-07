from flask import Flask, jsonify, render_template_string, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Simple clean JSON response
    if 'application/json' in request.headers.get('Accept', ''):
        return jsonify({
            "app": "Flask API",
            "status": "running",
            "version": "1.0"
        })

    # Minimal welcome page
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Welcome</title>
        <style>
            body {
                font-family: -apple-system, BlinkMacSystemFont, sans-serif;
                margin: 0;
                padding: 20px;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                background: #fafafa;
                color: #333;
                text-align: center;
                line-height: 1.5;
            }
            .card {
                background: white;
                padding: 2rem;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.05);
                max-width: 400px;
            }
            h1 {
                margin-top: 0;
                color: #222;
            }
            .status {
                display: inline-block;
                padding: 4px 8px;
                background: #e1f5fe;
                color: #0288d1;
                border-radius: 4px;
                font-size: 0.9em;
                margin-top: 1rem;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Flask API</h1>
            <p>A simple web service</p>
            <div class="status">Status: Running</div>
        </div>
    </body>
    </html>
    ''')

if __name__ == '__main__':
    # Ensure the app listens on all network interfaces
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
