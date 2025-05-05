from flask import Flask, jsonify, render_template_string, request
from datetime import datetime
import os
import platform

app = Flask(__name__)

@app.route('/')
def home():
    # Professional JSON response with metadata
    response_data = {
        "status": "success",
        "message": "Hello from Railway!",
        "metadata": {
            "service": "Flask API",
            "version": "1.0.0",
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "environment": os.getenv('FLASK_ENV', 'development'),
            "server": platform.node(),
            "documentation": "/docs"  # Optional: Add API docs endpoint
        },
        "links": {
            "self": request.url,
            "health": f"{request.url_root}health",
            "status": f"{request.url_root}status"
        }
    }

    # Simple HTML design for browser requests
    if 'text/html' in request.headers.get('Accept', ''):
        return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Flask API</title>
            <style>
                body { font-family: Arial, sans-serif; line-height: 1.6; 
                       margin: 0; padding: 20px; background: #f5f5f5; }
                .container { max-width: 800px; margin: 0 auto; background: white;
                             padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
                h1 { color: #2c3e50; border-bottom: 1px solid #eee; padding-bottom: 10px; }
                pre { background: #f8f9fa; padding: 15px; border-radius: 4px; 
                      overflow-x: auto; }
                .meta { color: #7f8c8d; font-size: 0.9em; margin-top: 20px; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>API Response</h1>
                <pre>{{ response }}</pre>
                <div class="meta">
                    <p>Server: {{ server }} | Environment: {{ env }}</p>
                </div>
            </div>
        </body>
        </html>
        ''', response=jsonify(response_data).get_data(as_text=True),
           server=platform.node(), env=os.getenv('FLASK_ENV', 'development'))

    return jsonify(response_data)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)