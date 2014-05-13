# Bottle & relationated
from bottle import *
# OS
import os
from os import path



@route('/')
def index():
	return template('index')


# Static routes: css, js, images, ...
@get('/<filename:re:.*\.js>')
def javascripts(filename):
	return static_file(filename, root=os.environ['OPENSHIFT_REPO_DIR']+'/wsgi/static/js')

@get('/<filename:re:.*\.css>')
def stylesheets(filename):
	return static_file(filename, root=os.environ['OPENSHIFT_REPO_DIR']+'/wsgi/static/css')

@get('/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
	return static_file(filename, root=os.environ['OPENSHIFT_REPO_DIR']+'/wsgi/static/img')

@get('/<filename:re:.*\.(eot|ttf|woff|svg)>')
def fonts(filename):
	return static_file(filename, root=os.environ['OPENSHIFT_REPO_DIR']+'/wsgi/static/fonts')

@get('/<filename:re:.*\.(doc|pdf)>')
def fonts(filename):
	return static_file(filename, root=os.environ['OPENSHIFT_REPO_DIR']+'/wsgi/static/resources')


# This must be added in order to do correct path lookups for the views
import os
from bottle import TEMPLATE_PATH

TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi/views/'))
application=default_app()

