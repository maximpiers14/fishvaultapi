from flask import Flask
from api_routes import api
from image_routes import images

app = Flask(__name__)

app.config.update({
    "SESSION_COOKIE_SAMESITE": "Lax",
    "SESSION_COOKIE_HTTPONLY": True
})

app.register_blueprint(api)
app.register_blueprint(images)

if __name__ == "__main__":
    app.run()