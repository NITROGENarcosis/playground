from flask import Blueprint, render_template, url_for, flash, g, redirect, request, \
    abort, current_app, session

import pymysql.cursors

#from contextlib import closing

home = Blueprint('home', __name__)

def connect_db():
    return pymysql.connect(host=current_app.config['DB_HOST'], 
                           user=current_app.config['DB_USER'],
                           password=current_app.config['DB_PASS'],
                           db=current_app.config['DATABASE'],
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)

@home.before_request
def before_request():
    g.db = connect_db()

@home.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

@home.route('/')
def show_entries():
    cur = g.db.cursor()
    sql = 'select id, title, text from entries order by id desc'
    cur.execute(sql)
    entries = [dict(id=row['id'], title=row['title'], text=row['text']) for row in cur.fetchall()]
    return render_template('home/show_entries.html', entries=entries)

@home.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    cur = g.db.cursor()
    cur.execute('insert into entries (title, text) values (%s, %s)', \
        (request.form['title'], request.form['text']))
    g.db.commit()
    flash('New entry was posted')
    return redirect(url_for('.show_entries'))

@home.route('/delete')
def delete_entry():
    if not session.get('logged_in'):
        abort(401)
    cur = g.db.cursor()
    cur.execute('delete from entries where id=%s', request.args.get('id', ''))
    g.db.commit()
    flash('entry deleted')
    return redirect(url_for('.show_entries'))

