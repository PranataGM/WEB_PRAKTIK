from flask import render_template, request, redirect, url_for, session, flash
from models.berita_model import BeritaModel
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def add_berita():
    judul = request.form['judul']
    tanggal = request.form['tanggal']
    rincian = request.form['rincian']
    file = request.files['gambar']

    if file and file.filename:
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))
    else:
        filename = None
    BeritaModel.add(judul, tanggal, rincian, filename)
    return redirect(url_for('berita'))

# def admin_dashboard():
#     berita_list = BeritaModel.get_all()
#     return render_template('admin_dashboard.html', berita=berita_list)

def edit_berita(id):
    berita = BeritaModel.get_by_id(id)
    
    if request.method == 'POST':
        judul = request.form['judul']
        tanggal = request.form['tanggal']
        rincian = request.form['rincian']
        file = request.files.get('gambar')
        
        if file and file.filename:
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
        else:
            filename = berita['gambar']

        BeritaModel.update(id, judul, tanggal, rincian, filename)
        flash('Berita berhasil diupdate', 'success')
        return redirect(url_for('berita'))
    return render_template('edit_berita.html', berita=berita)


def delete_berita(id):
    BeritaModel.delete(id)
    flash('Berita berhasil dihapus', 'success')
    return redirect(url_for('berita'))
