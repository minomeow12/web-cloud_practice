from flask import Flask, render_template, redirect, url_for, request
from model_sqlite3 import model


app = Flask(__name__)
db = model()


#home page
@app.route('/')
@app.route('/index.html')
def index():
   """
    Display the home page.

    :return: Rendered home page HTML.
    :rtype: str
    """
  return render_template('index.html')

#view the playlist
@app.route('/playlist')
def playlist():
      """
    Retrieve all songs and display the playlist.

    :return: Rendered playlist HTML.
    :rtype: str
    """
  entries = [ 
    dict(
      title=row[1], 
      artist=row[2],
      url=row[3],
      release_year=row[4]
    )
    for row in db.select()
  ]
  return render_template('playlist.html', entries=entries)

#add a song
@app.route('/add', methods=['GET','POST'])
def add():
  """
Display the Add Song form or process a new song submission.

:return: Rendered HTML for GET or a redirect for POST.
:rtype: str or werkzeug.wrappers.Response
"""
  if request.method == 'POST':
    db.insert(request.form['title'], request.form['artist'], request.form['url'], int(request.form['release_year']))
    return redirect(url_for('playlist'))
  return render_template('add.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)
