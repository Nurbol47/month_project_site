from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/profile')
def profile():
    return 'profile'


@app.route('/about')
def about():
    return 'about'


@app.route('/genres')
def genres():
    return render_template('genres.html')


if __name__ == '__main__':
    app.run(debug=True)

