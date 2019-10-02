import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    TOKEN = os.environ.get('TOKEN')
    HOST_URL = os.environ.get('HOST_URL')
    ADMINS = ['legalionion@gmail.com', 'playersoft1999@gmail.com']
