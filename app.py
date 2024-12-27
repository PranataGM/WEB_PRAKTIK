from flask import Flask, render_template, request, redirect, url_for, session, flash
import pymysql
from controllers.home_controller import home
from controllers.berita_controller import berita
from controllers.kontak_controller import kontak
from controllers.auth_controller import login, logout
from controllers.admin_controller import add_berita, edit_berita, delete_berita

app = Flask(__name__)
app.secret_key = 'secret_key_untuk_session'

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Routing
app.add_url_rule('/', view_func=home)
app.add_url_rule('/berita', view_func=berita)
app.add_url_rule('/kontak', view_func=kontak)
app.add_url_rule('/login', view_func=login, methods=['GET', 'POST'])
app.add_url_rule('/logout', view_func=logout)
app.add_url_rule('/admin/add', view_func=add_berita, methods=['POST'])
app.add_url_rule('/admin/edit/<int:id>', view_func=edit_berita, methods=['POST'])
app.add_url_rule('/admin/delete/<int:id>', view_func=delete_berita, methods=['GET'])

if __name__ == '__main__':
    app.run(debug=True)
