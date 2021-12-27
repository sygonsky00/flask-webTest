from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'webTest.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'#\xb1\x07\x96\xe4\xd4h\x12P\x11K\r$z\xc8\xae'