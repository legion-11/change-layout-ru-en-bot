import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    TOKEN = os.environ.get('TOKEN') or '772580322:AAHOJhc26cZbRkTPbBcGK801bmTCEGFQzQE'
    HOST_URL = os.environ.get('HOST_URL') or 'https://b337b007.ngrok.io'
    ADMINS = ['legalionion@gmail.com']
