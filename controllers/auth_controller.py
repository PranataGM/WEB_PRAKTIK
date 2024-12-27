from flask import render_template, request, redirect, url_for, session, flash

def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'admin123':
            session['user'] = 'admin'
            session['is_admin'] = True
            return redirect(url_for('berita'))
    return render_template('login.html')

def logout():
    session.pop('user', None)
    session.pop('is_admin', None)
    return redirect(url_for('login'))