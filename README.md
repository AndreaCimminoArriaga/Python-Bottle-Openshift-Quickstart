Python-Bottle-Openshift-Quickstart
==================================

A simple openshift template for bottle python framework.
Create a simple project:

	rhc app create <app-name> python-3.3

	cd <app-name>

Once in the directory delete all files and copy the files from this template.

To add dependainces to the python interpreter add them in the file setup.py, in the line:

	install_requires=['bottle', '<YOURDEPENDAINCE>']

The project structure is:

	./
		requirements.txt 	is a empty document
		setup.py 			as said before is a openshift config file
		wsgi.py 			another config file don't touch
		wsgi/
			application		is the entry point of the app, don't touch
			mybottleapp.py  This is the file you have to worl to add routes (alredy prepared to serve static files such as images, css and others from static folder)
			static/ 		contains (in different folders) all static files
				(...)
			views/			bottle will charge all the tpl templates from this folder
				index.tpl   the main template
