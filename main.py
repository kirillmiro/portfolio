#Импорт
from flask import Flask, render_template,request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Настройки базы данных (SQLite)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#Создание таблицы
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)  
    email = db.Column(db.String(120), nullable=False)
    text = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Feedback {self.email}>'
    
#Запуск страницы с контентом
@app.route('/feedback', methods=['POST']) 
def feedback():
    email = request.form.get('email')
    text = request.form.get('text')

    # Сохраняем данные в базе
    feedback = Feedback(email=email, text=text)
    db.session.add(feedback)
    db.session.commit()

    return f"Спасибо за ваш отзыв! Ваш комментарий сохранён."

@app.route('/')
def index():
    return render_template('index.html')
    
#Динамичные скиллы
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_html = request.form.get('button_html')
    button_discord = request.form.get('button_discord')
    button_db = request.form.get('button_db')
    return render_template('index.html', button_html=button_html, button_python=button_python, button_discord=button_discord, button_db=button_db)

if __name__ == "__main__":
    app.run(debug=True)