from flask.helpers import send_file
from flask import render_template, abort, flash, Blueprint
from Web.main.forms import UploadJavaForm
from random import randint
import shutil as zip
import secrets
import os
import logging

UPLOAD_FOLDER = '/path/to/'
ALLOWED_EXTENSIONS = {'java','txt'}

from gui.utils import nassi
from interpreter.NassiShneidermann import NassiShneidermanDiagram, OB

main = Blueprint('main', __name__)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def javaDatei(form_file):
    try:
        random_hex = secrets.token_hex(8)
        _, f_ext = os.path.splitext(form_file.filename)
        file_fname = random_hex + f_ext
        dirctory_path = os.path.abspath(os.path.join('Web', os.pardir))
        file_path = os.path.join(dirctory_path, './tmp/input', file_fname)
        form_file.save(file_path)
        return file_path
    except:
        flash('Hier ist was falsch gelaufen!')


@main.route('/', methods=['POST', 'GET'])
@main.route('/generator', methods=['POST','GET'])
def generator():
    form = UploadJavaForm()

    if form.validate_on_submit():
        if form.java.data:
            input_path = javaDatei(form.java.data)
            output_path = os.path.join(os.path.abspath(os.path.join('Web', os.pardir)), './tmp/input')
            outputname = str(randint(0, 100) )
            remove_tags = None 
            comments = None 
            behaviour = OB.RANDOM_NAME 
            types = None

            NSD = NassiShneidermanDiagram(True)
            output_directory = output_path + '/' + outputname
            
            # if font_filepath != None:
            #     NSD.set_font(font_filepath)

            try:
                if not os.path.exists(output_directory):
                    os.makedirs(output_directory)
            except OSError:
                logging.error('Error: Creating directory. ' +  output_directory)


            custom_tags = {"comments" : comments, "ignore" : remove_tags, "types" : types}
            
            NSD.load_from_file(input_path, custom_tags)
            NSD.convert_to_image(output_directory, on_conflict=behaviour)

            zip_path = os.path.join(os.path.abspath(os.path.join('Web', os.pardir)), f'../tmp/output/{outputname}')
            zip.make_archive(zip_path, 'zip', output_directory) 

            return send_file(zip_path + '.zip', as_attachment=True)

    return render_template('upload.html', title='Upload', legend='Upload', form=form )
    
