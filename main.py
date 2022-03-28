from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
import json
import os
app = Flask(__name__)
UPLOAD_FOLDER = 'files_to_print'
# UPLOAD_FOLDER = '/home/cloudprinter/mysite/files_to_print'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def hello_world():
    if request.method == "POST":
        if 'file' not in request.files:
            return "Please upload a file"
        
        file = request.files["file"]

        if file.filename == '':
            return "Please upload a valid file"

        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            return redirect("/?status=printing")
    else:
        return render_template("index.html")


@app.route('/upload_file', methods=["POST"])
def upload_file():
    if request.method == "POST":
        if 'file' not in request.files:
            return "Please upload a file"
        
        file = request.files["file"]

        if file.filename == '':
            return "Please upload a valid file"

        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            return redirect("/?status=uploaded")


@app.route('/get_files', methods=["GET"])
def get_files():
    if request.method == "GET":

        return json.dumps(os.listdir(app.config["UPLOAD_FOLDER"]))


if __name__ == "__main__":
    app.run(debug=True)