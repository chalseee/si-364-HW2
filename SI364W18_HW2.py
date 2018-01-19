## SI 364
## Winter 2018
## HW 2 - Part 1

## This homework has 3 parts, all of which should be completed inside this file.

## Add view functions and any other necessary code to this Flask application code below so that the routes
## described in the README exist and render the templates they are supposed to (all templates provided are inside
## the templates/ directory, where they should stay).

## As part of the homework, you may also need to add templates (new .html files) to the templates directory.

#############################
##### IMPORT STATEMENTS #####
#############################

from flask import Flask, request, render_template
#import FlaskForm
from wtforms import StringField, SubmitField, RadioField, ValidationError
from wtforms.validators import Required

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, ValidationError
from wtforms.validators import Required

import requests

#####################
##### APP SETUP #####
#####################

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hardtoguessstring'

####################
###### FORMS #######
####################

class AlbumEntryForm():
    name = StringField(label=u'Enter the name of an album', validators=[Required()])
    rating = RadioField(label=u'How much do you like this album (1 low, 3 high)', choices=['1', '2', '3'], validators=[Required()])
    submit = SubmitField(label="Submit")

####################
###### ROUTES ######
####################

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/user/<name>')
def hello_user(name):
    return '<h1>Hello {0}<h1>'.format(name)

@app.route('/artistinfo', methods=[ 'GET'])
def artist_info():
    if request.method == "GET":
        name = request.args['artist']
        url = 'https://itunes.apple.com/search?entity=musicTrack&term={}'.format(name)
        r = requests.get(url)
        artist = r.json()['results']
        objs = []
        for a in artist:
            objs.append({'trackName':a['trackName'], 'trackViewUrl':a['trackViewUrl']})
        return render_template('artist_info.html', objects=objs)

@app.route('/artistlinks')
def artist_links():
    return render_template('artist_links.html')

@app.route('/artistform')
def artist_form():
    return render_template('artistform.html')

@app.route('/specific/song/<artist_name>')
def specific_artist(artist_name):
    url = 'https://itunes.apple.com/search?entity=musicTrack&term={}'.format(artist_name)
    r = requests.get(url)
    objs = r.json()['results']
    return render_template('specific_artist.html', results=objs)

@app.route('/album_entry')
def album_entry():
    form_var = AlbumEntryForm()
    return render_template('album_entry.html', form=form_var)

@app.route('/album_result')
def album_data():
    return "str2"

if __name__ == '__main__':
    app.run(use_reloader=True,debug=True)
