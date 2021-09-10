from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')
    # return "<p>Hello, World!</p>"

# this main method is written to run the above the app, and run in the debug mode, so if the debug comes, show me error in the browser only!!
if __name__ == '__main__':
    app.run(debug=True, port = 8000)
# to change the port name just write the port = "new port no" , default the port is save to the '5000'

# product page
@app.route("/products")
def hello_world():
    return "this is a product page"

# remember there are 2 directories static and templates, this both directories should always have different folders , hame kabhi bhi ek ke andar ek directories ko nahi rakhna hai, means static ke andar templates ko nhi rakhna waise hi , templates ke andar static ko nhi rakhna and more imp, never put thuis both the folder into the virtual env folder.

