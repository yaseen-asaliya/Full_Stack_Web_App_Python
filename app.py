from flask import Flask

app = Flask(__name__)

@app.route('/test')
def hello():
    return 'test'

if __name__ == '_main_':
    #Run the application on defult port 5000 
    #Just for local development of the API
    app.run(debug=True,threaded=True)