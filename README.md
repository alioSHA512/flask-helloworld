##比 flask 官方文档更简单的一个示例

    Type "help", "copyright", "credits" or "license" for more information.
    >>> 
    >>> from flask import Flask
    >>> 
    >>> app = Flask('test')
    >>> 
    >>> from flask.ext.helloworld import HelloWorld
    >>> from flask_helloworld import HelloWorld as HW2
    >>> 
    >>> hw = HelloWorld(app)
    >>> 
    >>> hw.state
    'Hello World!'
    >>>
