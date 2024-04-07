from flask import Flask


app = Flask(__name__)

@app.route("/")#URL leading to method
def hello(): # Name of the method
 return("Hello World!") 

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080')  #Changing port to 8080