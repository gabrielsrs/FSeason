from app import app

with app.app_context():
    from routes import handle

    app.register_blueprint(handle)

if __name__ == "__main__":
    app.run(
            debug=eval(app.config["FLASK_DEBUG"]),
            host=app.config["SERVER"],
            port=int(app.config["PORT"])
    )
