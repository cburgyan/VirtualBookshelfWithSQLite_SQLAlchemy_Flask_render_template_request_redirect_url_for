from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

all_books = []


@app.route('/')
def home():
    return render_template('index.html', books=all_books)


@app.route("/add", methods=['POST', 'GET'])
def add():
    global all_books
    print('hi')
    if request.method == 'POST':
        print('POSTTTT')
        temp_dict = {"title": request.form["title"], 'author': request.form["author"], 'rating': request.form["rating"]}
        all_books.append(temp_dict)
    else:
        print('GETTTT')
    print(all_books)
    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True)

