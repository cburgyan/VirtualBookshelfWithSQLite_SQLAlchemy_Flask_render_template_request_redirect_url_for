from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Create Flask
app = Flask(__name__)

# Create Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Define Table/Record
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'


# Create Table
db.create_all()


@app.route('/')
def home():
    return render_template('index.html', books=Book.query.all())

@app.route('/<id>')
def delete_page(id):
    book_for_deletion = Book.query.filter_by(id=id).first()
    db.session.delete(book_for_deletion)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/add", methods=['POST', 'GET'])
def add():
    print('hi')
    if request.method == 'POST':
        print('POSTTTT')

        new_book = Book(title=request.form['title'], author=request.form['author'], rating=request.form['rating'])
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        print('GETTTT')
    print(Book.query.all())
    return render_template('add.html')


@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit_rating_page(id):
    book_to_update = Book.query.filter_by(id=id).first()
    if request.method == 'POST':
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('edit_rating.html', book=book_to_update)


if __name__ == "__main__":
    app.run(debug=True)

