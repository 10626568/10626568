from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FileField
# from flask_uploads import configure_uploads, IMAGES, UploadSet
# from werkzeug.utils import secure_filename

app = Flask(__name__, template_folder="templates")
app.config['UPLOADED_IMAGES_DEST'] = 'uploads/images'
app.config['SECRET_KEY'] = 'secretkey'


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
        return render_template('submission.html')
    else:
        return "except"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080') # indent this line

