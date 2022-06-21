# importing the required libraries
import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

# initialising the flask app
app = Flask(__name__)

# Max size of the file
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024

# Creating the upload folder
upload_folder = "uploads/"
if not os.path.exists(upload_folder):
   os.mkdir(upload_folder)

# Configuring the upload folder
app.config['UPLOAD_FOLDER'] = upload_folder

# configuring the allowed extensions
allowed_extensions = ['txt']

def check_file_extension(filename):
    return filename.split('.')[-1] in allowed_extensions

# The path for uploading the file
@app.route('/')
def upload_file():
   return render_template('upload.html')

@app.route('/upload', methods = ['GET', 'POST'])
def uploadfile():
   if request.method == 'POST': # check if the method is post
      f = request.files['file'] # get the file from the files object
      # Saving the file in the required destination
      if check_file_extension(f.filename):
         f.save(os.path.join(app.config['UPLOAD_FOLDER'] ,secure_filename(f.filename))) # this will secure the file
         return 'file uploaded successfully' # Display thsi message after uploading
      else:
         return 'The file extension is not allowed'

if __name__ == '__main__':
   app.run() # running the flask app