from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def about():  # put application's code here
    return 'Hello World! from Ryan Hoang! I am adding my first code change.'
@app.route('/about')
def about():
    return render_template('about.html')
if __name__ == '__main__':
    app.run()