# #url_for(fun_name,optional)
# from flask import Flask,redirect,url_for

# app = Flask(__name__)

# @app.route('/admin')
# def hello_admin():
#     return 'Hello Admin'

# @app.route('/guest/<guest>')
# def hello_guest(guest):
#     return 'Hello %s as Guest' % guest

# @app.route('/public')
# def hello_public():
#     return 'Hello public!'

# @app.route('/user/<name>')
# def hello_user(name):
#     if name == 'admin':
#         return redirect(url_for('hello_admin'))
#     elif name == 'guest':
#         return redirect(url_for('hello_guest',guest=name))
#     else:
#         return redirect(url_for('hello_public'))
    
# if __name__ == '__main__':
#     app.run(debug=True)

