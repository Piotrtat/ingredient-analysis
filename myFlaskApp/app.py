from flask import Flask, render_template, request
from data import Articles
from wtforms import Form, StringField, TextField, PasswordField, validators


app = Flask(__name__)

Articles = Articles()



@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/articles')
def articles():
    return render_template('articles.html', articles = Articles)

@app.route('/article/<string:id>/')
def article(id):
    return render_template('article.html', id=id)

class IngredientsForm(Form):
    name = StringField('Enter the ingredient you are interested in:', [validators.Length(min=1, max=50)])

@app.route('/ingredients', methods=['GET', 'POST'])
def ingredients():
    form = IngredientsForm(request.form)
    if request.method == 'POST' and form.validate():
        return render_template('ingredients.html')
    return render_template('ingredients.html', form=form)

if __name__ == '__main__':
    app.run()
