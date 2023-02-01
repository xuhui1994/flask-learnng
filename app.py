from flask import Flask,render_template

app = Flask(__name__)


#@app装饰器默认支持GET，def是视图函数
@app.route('/',methods=["POST","GET"])
def hello_world():  # put application's code here
    # return 'Hello World!'
    return render_template("index.html")

@app.route('/order/<order_id>',methods=["POST","GET"])
def get_order_id(order_id):
    #需要在视图函数()中填入参数名
    print(type(order_id)) #默认为字符串
    return ("order_id: %s"%order_id)

if __name__ == '__main__':
    app.run()
