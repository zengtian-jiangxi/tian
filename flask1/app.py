from flask import Flask,render_template,make_response,request
from flask1 import  settings



app=Flask(__name__,template_folder='templates' )   #template_folder='templates'   默认

app.config.from_object(settings)



#首页
@app.route('/')
def fun1():
    return render_template('shou.html')



@app.route('/a')
def tet():
    return render_template('登入界面.html')


@app.route('/index',methods=['GET','POST'])
def index():
    wood=make_response('hesf')
    print(request.path)
    print(request.args)
    var = request.args.get('username')
    print(var)
    #如果请求方法是post请求，则需要通过request.from 取值
    return wood

# @app.route('/tijiao')
# def fun1():
#     return '1'


@app.route('/register')
def register():
    return 'hello'
if __name__ == '__main__':
    print(app.url_map)
    app.run(host='127.0.0.1',port='5100',debug=True)
