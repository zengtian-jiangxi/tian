from flask import Flask,render_template

app=Flask(__name__)


@app.route('/')
def fun():
    name=123
    return render_template('students.html',name=name)

if __name__ == '__main__':
    app.run()