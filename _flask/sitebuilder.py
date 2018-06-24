import sys

from flask import Flask, render_template, redirect, url_for, flash, request
#from flask import send_file
from flask_flatpages import FlatPages
from flask_frozen import Freezer

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)

@app.route('/')
def index():
    return render_template('index.html', pages=pages)

@app.route('/posts')
def posts():
    print "HERE"
    for i in pages:
        print i
    return render_template('posts.html', pages=pages)

@app.route('/tag/<string:tag>/')
def tag(tag):
    tagged = [p for p in pages if tag in p.meta.get('tags', [])]
    return render_template('tag.html', pages=tagged, tag=tag)

@app.route('/<path:path>/')
def page(path):
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)
'''
@app.route('/resume/')
def resume():
    return return_files('static/files/resume.pdf', 'resume.pdf')

def return_files(path, name):
    try:
	return send_file(path, attachment_filename=name)
    except Exception as e:
	return str(e)
'''            
if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(port=5000)