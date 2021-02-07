from flask import Flask, render_template, request, redirect, url_for
from flask1 import settings
app=Flask(__name__)
app.config.from_object(settings)
name=None
#学生信息系统
@app.route('/')
def fun():
    return render_template('shou.html')
@app.route('/student')
def student():
    return render_template('student_index.html')
@app.route('/student_index',methods=['GET','POST'])
def student_index():
    global name
    name=request.form.get('username')
    print(request.form.get('username'))

    return redirect(url_for('students'))    #url_for(函数名)
    # return '登录成功'
@app.route('/students')
def students(name):
    name=name
    return render_template('students.html',name=name)




# 教师管理系统
@app.route('/teacher')
def teacher():
    return '这是教师系统'

if __name__ == '__main__':
    app.run(debug=True)
