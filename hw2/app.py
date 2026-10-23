from flask import Flask, render_template, redirect, url_for, request
from urllib.parse import quote
from model_sqlite3 import model


app = Flask(__name__)
db = model()


#home page
@app.route('/')
@app.route('/index.html')
def index():
  return render_template('index.html')

#view the playlist
@app.route('/playlist')
def playlist():
  entries = [ 
    dict(
      title=row[1], 
      artist=row[2],
      url=row[3],
    )
    for row in db.select()
  ]
  return render_template('playlist.html', entries=entries)

#add a song
@app.route('/add', methods=['GET','POST'])
def add():
  """
  Accept POST requests, and process the form;
  redirect to playlist when completed.
  """
  if request.method == 'POST':
    db.insert(request.form['title'], request.form['artist'], request.form['url'])
    return redirect(url_for('playlist'))
  return render_template('add.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)
