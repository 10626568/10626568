from flask import Flask, render_template, request
import os

app = Flask(__name__, template_folder="templates")
app.config['UPLOADED_IMAGES_DEST'] = 'uploads'


@app.route("/")  # URL leading to method
def index():  # Name of the method
    return render_template("index.html")


@app.route("/submission", methods=['GET', 'POST'])
def submission():
    if request.method == "POST":
        fname = request.form['fname']
        # lname = request.form['lname']
        files = request.files['photo']
        file_name = files.filename
        files.save(os.path.join(app.config['UPLOADED_IMAGES_DEST'],file_name))
        with open(os.path.join(app.config['UPLOADED_IMAGES_DEST'],file_name), 'rb') as f:
            bin_data = f.read()
        #pyodbc.Binary(bin_data)
        return render_template('submission.html')
    else:
        return "except"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080') # indent this line

