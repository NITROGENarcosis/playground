import sqlite3

from flask import Flask, request, session, g, redirect, url_for, \
	abort, render_template, flash
from contextlib import closing

#config
DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'dev_key'
USERNAME = 'admin'
PASSWORD = 'qwerty'

# create app
app = Flask(__name__)
app.config.from_object(__name__)

# db connector function
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

# removed for moving to mariadb
# db init function
#def init_db():
#    with closing(connect_db() ) as db:
#        with app.open_resource('schema.sql', mode='r') as f:
#            db.cursor().executescript(f.read())
#        db.commit()

# set db access
@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None )
    if db is not None:
        db.close()
# routes
@app.route('/')
def show_entries():
    cur = g.db.execute('select id, title, text from entries order by id desc')
    entries = [dict(id=row[0], title=row[1], text=row[2]) for row in cur.fetchall()]
    return render_template('show_entries.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into entries (title, text) values (?, ?)', \
        [request.form['title'], request.form['text']])
    g.db.commit()
    flash('New entry was posted')
    return redirect(url_for('show_entries'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'bad user'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'bad pass'
        else:
            session['logged_in'] = True
            flash('login good')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('logged out')
    return redirect(url_for('show_entries'))

@app.route('/delete')
def delete_entry():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('delete from entries where id=?', request.args.get('id', ''))
    g.db.commit()
    flash('entry deleted')
    return redirect(url_for('show_entries'))

#fire up server if standalone
if __name__ == '__main__':
    app.run(host='0.0.0.0')

