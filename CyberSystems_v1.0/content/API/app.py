# importing the required libraries
import os
import json
import io
from flask import Flask, render_template, request, Response
from werkzeug.utils import secure_filename
from rpmDecoder import decoder
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

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
allowed_extensions = ['txt', 'log']

def check_file_extension(filename):
    return filename.split('.')[-1] in allowed_extensions

# The path for uploading the file
@app.route('/')
def upload_file():
   return render_template('upload.html')


@app.route('/upload', methods = ['POST'])
def uploadfile():
   if request.method == 'POST': # check if the method is post
      f = request.files['file'] # get the file from the files object
      # Saving the file in the required destination
      if check_file_extension(f.filename):
         f.save(os.path.join(app.config['UPLOAD_FOLDER'] ,secure_filename(f.filename))) # this will secure the file
         #return 'file uploaded successfully' # Display thsi message after uploading
         data = json.loads(decoder("C:/Users/austi/Hugo/Cyber_Website_Temp/ProjectFile/CyberSystems_temp/CyberSystems_v1.0/uploads/" + f.filename))
         fig = Figure()
         axis = fig.add_subplot(1, 1, 1)
         xs = data["rpmTime"]
         ys = data["rpm"]
         axis.plot(xs, ys)
         output = io.BytesIO()
         FigureCanvas(fig).print_png(output)
         return Response(output.getvalue(), mimetype='image/png')
      else:
         return 'The file extension is not allowed'








######
if __name__ == '__main__':
   app.run() # running the flask app

