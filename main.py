from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop_book.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    text = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Книга: {self.title}"

@app.route('/')
@app.route('/home')
def home():
    books = Book.query.all()
    return render_template('index.html', data=books)


@app.route('/profile')
def profile():
    return 'profile'


@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == "POST":
        title = request.form['title']
        author = request.form['author']
        price = request.form['price']
        text = request.form['text']

        book = Book(title=title, author=author, price=price, text=text)

        try:
            db.session.add(book)
            db.session.commit()
            return redirect('/home')
        except:
            return "Получилось ошибка"
    else:
        return render_template('create.html')


@app.route('/genres')
def genres():
    books = Book.query.all()
    return render_template('genres.html', data=books)


if __name__ == '__main__':
    app.run(debug=True)

