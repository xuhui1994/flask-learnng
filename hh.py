from flask import Flask, current_app, redirect, url_for, request

# 实例化app
app = Flask(import_name=__name__)

# 通过methods设置POST请求
@app.route('/form', methods=["POST"])
def form_request():

    # 接收post请求的form表单参数
    user_name = request.form.get('user_name')
    user_age = request.form.get('user_age')

    return "user_name = %s, user_age = %s" % (user_name,user_age)

if __name__ == '__main__':
    app.run()
