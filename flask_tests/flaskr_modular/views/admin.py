import pymysql.cursors

from flask import Blueprint, request, session, g, redirect, url_for, \
    abort, render_template, flash, current_app
from contextlib import closing

admin = Blueprint('admin', __name__)

# db connector function
def connect_db():
    return pymysql.connect(host=current_app.config['DB_HOST'], 
                           user=current_app.config['DB_USER'],
                           password=current_app.config['DB_PASS'],
                           db=current_app.config['DATABASE'],
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
# set db access
@admin.before_request
def before_request():
    g.db = connect_db()

@admin.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None )
    if db is not None:
        db.close()

@admin.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        cur = g.db.cursor()
        sql = 'select `id` from `login` where `username` = %s and `password` = %s'
        cur.execute(sql, (request.form['username'], request.form['password']))
        if not cur.fetchall():
            error = 'bad login'
        else:
            session['logged_in'] = True
            flash('login good')
            return redirect(url_for('home.show_entries'))
    return render_template('admin/login.html', error=error)

@admin.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('logged out')
    return redirect(url_for('home.show_entries'))
