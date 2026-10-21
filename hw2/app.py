from flask import Flask, render_template
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
    for row in model.select()
  ]
  return render_template('playlist.html', entries=entries)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)
