from flask import Flask,render_template,request,make_response

app = Flask(__name__)

@app.route('/')
def test():
  return 'Hello'

@app.route('/square', methods=['GET'])
def squarenumber():
    if request.method == 'GET':
        if(request.args.get('num') == None):
            return render_template('8.html')
        elif(request.args.get('num') == ''):
            return "<html><body><h1>Invalid number</h1></body></html>"
        else:
            number = request.args.get('num')
            sq= int(number) * int(number)
            return render_template('answer.html',squareofnum = sq,num = number)

if __name__ == '__main__':
    app.run(debug=True)