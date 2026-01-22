import os
from flask import Flask, render_template, redirect

app = Flask(__name__)

# Ссылка на твой файл в Google Drive
DRIVE_LINK = "https://drive.google.com/uc?export=download&id=17P6kKliwJHqVWqNlT4o-NlwMeZn-F-Mr"

@app.route('/')
def home():
    # ВОТ ОНА! Эта строчка говорит: "Возьми дизайн из templates/index.html"
    return render_template('index.html')

@app.route('/download')
def download():
    return redirect(DRIVE_LINK)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
