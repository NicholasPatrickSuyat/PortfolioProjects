# UPDATE the update method to where they can update one at a time
from flask import jsonify, request, abort, Blueprint
import psycopg2
from db import conn


conn = psycopg2.connect(
    """
    dbname=portfolioflask user=postgres host=localhost port=5432
    """
)

bp = Blueprint("games", __name__, url_prefix="/games")


@bp.route('', methods=['GET'])
def index():
    cur = conn.cursor()
    cur.execute("SELECT * FROM games;")
    rows = cur.fetchall()
    result = []
    for row in rows:
        info = {'id': row[0], 'game_title': row[1],
                'genre': row[2], 'developer_name': row[3]}
        result.append(info)
    return jsonify(result)


@bp.route('/<int:id>', methods=['GET'])
def get_id(id):
    if id is None:
        return abort(400)
    cur = conn.cursor()
    cur.execute("SELECT * FROM games WHERE id = %s;", (id,))
    rows = cur.fetchall()
    result = []
    for row in rows:
        info = {'id': row[0], 'game_title': row[1],
                'genre': row[2], 'developer_name': row[3]}
        result.append(info)
    return jsonify(result)


@bp.route('', methods=['POST'])
def create():
    data = request.get_json()

    if data is not None:
        if 'game_title' in data and 'genre' in data and 'developer_name' in data:
            game_title = data['game_title']
            genre = data['genre']
            developer_name = data['developer_name']

            try:
                cur = conn.cursor()
                cur.execute(
                    "INSERT INTO games (game_title, genre, developer_name) VALUES (%s, %s, %s)", (game_title, genre, developer_name))
                conn.commit()
                cur.close()

                return jsonify(success=True)
            except psycopg2.Error as e:
                conn.rollback()
                return abort(500)
        else:
            return abort(400)
    else:
        return abort(400)


@bp.route('/<int:id>', methods=['PATCH', 'PUT'])
def update(id):
    data = request.get_json()

    if 'game_title' in data and 'genre' in data and 'developer_name' in data:
        game_title = data['game_title']
        genre = data['genre']
        developer_name = data['developer_name']
        try:
            cur = conn.cursor()
            cur.execute(
                "UPDATE games SET game_title = %s, genre = %s, developer_name = %s WHERE id = %s ", (game_title, genre, developer_name, id))
            conn.commit()
            cur.close()

            return jsonify(True)
        except psycopg2.Error as er:
            conn.rollback()
            return abort(500)
    else:
        return abort(400)


@bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM games WHERE id = %s", (id,))
        conn.commit()
        return jsonify("Deletion Success!")

    except psycopg2.Error as er:
        conn.rollback()
        return abort(400)
