from flask import Flask

# ده إنشاء التطبيق
app = Flask(__name__)

# دي الصفحة الرئيسية للموقع
@app.route('/')
def home():
    return """
    <html>
        <head><title>Mazen Mohamed</title></head>
        <body style="background-color: #121212; color: #00ff00; text-align: center; font-family: sans-serif; padding-top: 50px;">
            <h1>Welcome to Mazen's World</h1>
            <p>Software Engineer in the making...</p>
            <hr style="width: 50%; border: 1px solid #333;">
            <div style="margin-top: 20px;">
                <button onclick="alert('Success!')" style="padding: 10px 20px; background: #00ff00; border: none; cursor: pointer;">Click Me</button>
            </div>
        </body>
    </html>
    """

# تشغيل السيرفر
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
