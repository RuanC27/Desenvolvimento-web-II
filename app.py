from flask import Flask
from controllers.StaticController import static_routes
from controllers.ProblemaController import problema_routes
from controllers.AutorController import autor_routes

app = Flask(__name__)

app.register_blueprint(static_routes)
app.register_blueprint(problema_routes)
app.register_blueprint(autor_routes)

if __name__ == '__main__':
    app.run(debug=True)
