from flask import Flask, jsonify, render_template_string
import os

app = Flask(__name__)

def get_twitter_style_page():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Welcome to Flask</title>
        <style>
            body {
                font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
                background-color: #15202B;
                color: #FFFFFF;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }
            .container {
                max-width: 600px;
                width: 100%;
                padding: 20px;
            }
            .card {
                background-color: #192734;
                border-radius: 16px;
                padding: 24px;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
            }
            .header {
                display: flex;
                align-items: center;
                margin-bottom: 20px;
            }
            .logo {
                color: #1DA1F2;
                font-size: 28px;
                font-weight: bold;
                margin-right: 10px;
            }
            .title {
                font-size: 24px;
                font-weight: bold;
            }
            .content {
                font-size: 18px;
                line-height: 1.5;
                margin-bottom: 20px;
            }
            .json-response {
                background-color: #253341;
                padding: 15px;
                border-radius: 8px;
                font-family: monospace;
                white-space: pre-wrap;
                margin-top: 20px;
                font-size: 14px;
            }
            .footer {
                margin-top: 20px;
                font-size: 14px;
                color: #8899A6;
                text-align: center;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="card">
                <div class="header">
                    <div class="logo">𝕏</div>
                    <div class="title">Welcome to Flask</div>
                </div>
                <div class="content">
                    Your Flask app is successfully running on Railway!
                </div>
                <div class="json-response">
                    {"status": "success", "message": "Hello from Railway!"}
                </div>
                <div class="footer">
                    Powered by Flask & Railway
                </div>
            </div>
        </div>
    </body>
    </html>
    """

@app.route('/')
def home():
    # Return HTML for browsers, JSON for API requests
    user_agent = request.headers.get('User-Agent', '').lower()
    if 'mozilla' in user_agent:  # Browser request
        return render_template_string(get_twitter_style_page())
    else:  # API request
        return jsonify({"status": "success", "message": "Hello from Railway!"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)