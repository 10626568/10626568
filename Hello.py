from flask import Flask, render_template
app = Flask(__name__, template_folder="templates")


@app.route("/")  # URL leading to method
def index():  # Name of the method
    return render_template("index.html")  # indent this line



if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080') # indent this line
