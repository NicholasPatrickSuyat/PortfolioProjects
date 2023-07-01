from users import bp as users_bp
from library import bp as library_bp
from games import bp as game_bp
from store import bp as store_bp

from flask import Flask


app = Flask(__name__)

app.register_blueprint(users_bp)
app.register_blueprint(library_bp)
app.register_blueprint(game_bp)
app.register_blueprint(store_bp)

app.run(host="localhost", port=5000, debug=True)
