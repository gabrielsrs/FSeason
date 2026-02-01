from app import create_app

if __name__ == "__main__":
    app = create_app()

    app.run(
            debug=app.config["FLASK_DEBUG"],
            host=app.config["SERVER"],
            port=app.config["PORT"]
    )
