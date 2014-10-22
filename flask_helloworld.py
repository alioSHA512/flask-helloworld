from flask.ext.pymongo import PyMongo


class HelloWorld(object):

    def __init__(self, app=None, config_prefix='HELLOWORLD'):
        if app is not None:
            self.init_app(app, config_prefix=config_prefix)

    def init_app(self, app, config_prefix='HELLOWORLD'):
        if 'helloworld' not in app.extensions:
            app.extensions['helloworld'] = {}
        
        if config_prefix in app.extensions['helloworld']:
            raise Exception('duplicate config_prefix "%s"' % config_prefix)

        self.state = "Hello World!"
