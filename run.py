# # an object of WSGI application 
# from flask import Flask	 
# app = Flask(__name__) # Flask constructor 

# # A decorator used to tell the application 
# # which URL is associated function 
# # @app.route('/')	 
# # def hello(): 
# # 	return 'HELLO Flask'

# def hello_world(): 
#    return 'hello world' 
# app.add_url_rule('/', '/hello_world', hello_world) 
 
# if __name__=='__main__': 
#     app.debug = True
#     app.run() 
   
import flask

app = flask.Flask(__name__)


class API:
    def __init__(self):
        app.add_url_rule("/", view_func=self.hello)

    def hello(self):
        return flask.Response("hello", 200)


if __name__ == "__main__":
    API()
    app.run()
