from flask import Flask, jsonify, make_response, render_template

application = Flask(__name__)
application.config['SECRET_KEY'] = 'Demo'


@application.route("/")
def hello_from_root():
    return jsonify(message='Hello, Hope you are doing well!')


@application.route("/home")
def hello():
    return render_template('index.html')


@application.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)


# application.register_blueprint(user_app, url_prefix='/rest/user')

if __name__ == '__main__':
    application.run(host="localhost", port=8080, debug=True)
