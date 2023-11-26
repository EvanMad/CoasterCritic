WTF_CSRF_ENABLED = True
SECRET_KEY = '\x8dO\xedb\xbf\xd2\xab\xb9\xfe\n\xb9I\xcbY\xa5\x18im!?\x8e\xafj\xae'

import os
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True