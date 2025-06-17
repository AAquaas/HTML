from flask import Flask, render_template
import random

app = Flask(__name__)
app.config['DEBUG'] = True



@app.route('/')
def index():
    return render_template("index.html")

@app.route('/hello')
def hello():
    message = "<h1>Here's a random number: {0}</h1> <h2>hhh</h2><h3>hi </h3> <p>hello</p>"
    num = random.randint(1, 25)
    return render_template("random.html")

@app.route('/goodbye')
def goodbye():
   message = "<h2>This is the second page!</h2>"
   return message

@app.route('/thanks')
def thanks():
        person = "Bob"
        action = "reading"
        end = "Thanks"
        writer = "Ryan"
        return render_template("tynote.html", name=person, verb=action, gift="book", noun="person", closing_word=end, author=writer)


@app.route('/coffee.co/home')

def home_page():
    return render_template("coffeeco_home.html")

@app.route('/coffee.co/order')

def order_page():
    return render_template("coffeeco_order.html")

if __name__ == '__main__':
    app.run()


