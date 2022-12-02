from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FileField

app = Flask(__name__, template_folder="templates")
Allowed_Extensions = ['jpg','jpeg','png']


class myForms(FlaskForm):
    image = FileField('photo')

@app.route("/")  # URL leading to method
def index():  # Name of the method
    form = myForms()
    return render_template("index.html", form=form)


@app.route("/submission", methods=['GET', 'POST'])
def submission():
    if request.method == "POST":
        fname = request.form['fname']
        # lname = request.form['lname']
        image = request.files['photo']
        print(image)
        return render_template('submission.html')
    else:
        return "except"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080') # indent this line
