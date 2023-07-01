# UPDATE the update method to where they can update one at a time
from flask import jsonify, request, abort, Blueprint
import psycopg2
from db import conn


conn = psycopg2.connect(
    """ 
    dbname=portfolioflask user=postgres host=localhost port=5432
    """
)

bp = Blueprint("library", __name__, url_prefix="/library")


@bp.route('', methods=['GET'])
def index():
    cur = conn.cursor()
    cur.execute("SELECT * FROM library;")
    rows = cur.fetchall()
    result = []
    for row in rows:
        info = {'id': row[0], 'genre': row[1], 'game_id': row[2]}
        result.append(info)
    return jsonify(result)


@bp.route('/<int:id>', methods=['GET'])
def get_id(id):
    if id is None:
        return abort(400)
    cur = conn.cursor()
    cur.execute("SELECT * FROM library WHERE id = %s;", (id,))
    rows = cur.fetchall()
    result = []
    for row in rows:
        info = {'id': row[0], 'genre': row[1], 'game_id': row[2]}
        result.append(info)
    return jsonify(result)
    


@bp.route('', methods=['POST'])
def create():
    data = request.get_json()
    if data is not None:
        if 'genre' in data and 'game_id' in data:
            genre = data['genre']
            game_id = data['game_id']

            try:
                cur = conn.cursor()
                cur.execute(
                    "INSERT INTO library (genre, game_id) VALUES (%s, %s)", (genre, game_id))
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

    if 'genre' in data and 'game_id' in data:
        genre = data['game_id']
        game_id = data['game_id']

        try:
            cur = conn.cursor()
            cur.execute(
                "UPDATE library SET genre = %s, game_id = %s WHERE id = %s ", (genre, game_id, id))
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
        cur.execute("DELETE FROM library WHERE id = %s", (id,))
        conn.commit()
        return jsonify(True)

    except:
        return abort(400)