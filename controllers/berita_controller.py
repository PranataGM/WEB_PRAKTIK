from flask import render_template
from models.berita_model import BeritaModel

def berita():
    berita_list = BeritaModel.get_all()
    return render_template('berita.html', berita=berita_list)