from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello():  # put application's code here

    fun_courses = ['BMGT302','BMGT402','BMGT407']

    return render_template('hello.html', courses=fun_courses)

@app.route('/about')
def about():
    return render_template('about.html')



@app.route('/favorite-course')
def favorite_course():
    print('Subject: ' + request.args.get('subject'))
    print('Course Number: ' + request.args.get('course_number'))

    return render_template('favorite-course.html')



@app.route('/contact', methods=['GET','POST'])
def contact():
    if request.method == 'POST':
        return render_template('contact.html', form_submitted=True)
    else:
        return render_template('contact.html')
if __name__ == '__main__':
    app.run()




