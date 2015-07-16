import os
from flask import Flask, request, redirect, url_to,send_from_directory
from werkzeug import secure_filename

UPLOAD_FOLDER = 'static/images/stock'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_files(filename):
	return '.' in file and filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS

@app_route('/upload',methods=["GET","POST"])
def upload_file():
	if request.method == "POST":
		file = request.files['shoe_upload']
		if file and allowed_files(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file', filename=filename))
    return

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)