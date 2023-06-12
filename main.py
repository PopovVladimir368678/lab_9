import os

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'lab9.db')
db = SQLAlchemy(app)

@app.route('/')
def main():
    return render_template('lab9.html')

@app.route('/find', methods=['POST'])
def find(title='', link=''):
    title = request.form['title']
    link = request.form['link']
    if title != '':
        entities = Entity.query.filter_by(title=title).all()
        return render_template('lab9.html', entities=entities)
    elif link != '':
        entities = Entity.query.filter_by(link=link).all()
        return render_template('lab9.html', entities=entities)
    else:
        return render_template('lab9.html')

@app.route('/add', methods=['POST'])
def add():
    title = request.form['title']
    link = request.form['link']
    entity = Entity(title=title, link=link)
    db.session.add(entity)
    db.session.commit()
    return render_template('lab9.html')

class Entity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    link = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Entity {self.title}>'

