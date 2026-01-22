from flask import Flask, render_template, redirect

app = Flask(__name__)

# Твоя ссылка на Google Drive
DRIVE_LINK = "https://drive.google.com/uc?export=download&id=17P6kKliwJHqVWqNlT4o-NlwMeZn-F-Mr"

@app.route('/')
def index():
    # Показываем главную страницу
    return render_template('index.html')

@app.route('/download')
def download_file():
    # Когда нажимают кнопку, Python сам перекидывает на файл
    print("Кто-то нажал кнопку скачать!")
    return redirect(DRIVE_LINK)

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
