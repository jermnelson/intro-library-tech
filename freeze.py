__author__ = "Jeremy Nelson"

from flask_frozen import Freezer
from run import app

app.config['FREEZER_BASE_URL'] = 'https://jermnelson.github.io/intro-library-tech/'
app.config['FREEZER_DESTINATION'] = 'docs'


freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
