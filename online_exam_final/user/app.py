from flask import Flask
from routes.user_routes import exam_routes

app = Flask(__name__)

# Register routes
app.register_blueprint(exam_routes)

if __name__ == "__main__":
    app.run(debug=True, port=5009)
