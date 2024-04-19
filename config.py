
import os

# get the base directory of this folder
# used only when using a local database
basedir = os.path.abspath(os.path.dirname(__file__))
# "C:\Users\Geri\Documents\coding_temple\week6\flask_blog_api"

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    
    FLASK_APP = os.environ.get('FLASK_APP')