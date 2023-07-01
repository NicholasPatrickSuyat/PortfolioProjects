# UPDATE the update method to where they can update one at a time
from flask import jsonify, request, abort, Blueprint
import psycopg2
from db import conn


conn = psycopg2.connect(
    """ 
    dbname=portfolioflask user=postgres host=localhost port=5432
    """
)

bp = Blueprint("users", __name__, url_prefix="/users")


@bp.route('', methods=['GET'])
def index():
    cur = conn.cursor()
    cur.execute("SELECT * FROM users;")
    rows = cur.fetchall()
    result = []
    for row in rows:
        info = {'id': row[0], 'username': row[1], 'email': row[2],
                'library_id': row[3], 'store_id': row[4]}
        result.append(info)
    return jsonify(result)


@bp.route('/<int:id>', methods=['GET'])
def get_id(id):
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE id = %s;", (id,))
    rows = cur.fetchall()
    result = []
    for row in rows:
        info = {'id': row[0], 'username': row[1], 'email': row[2],
                'library_id': row[3], 'store_id': row[4]}
        result.append(info)
    return jsonify(result)


@bp.route('', methods=['POST'])
def create():
    data = request.get_json()

    if data is not None:
        if 'username' in data and 'password' in data and 'email' in data and library_id in data and store_id in data:
            username = data['username']
            password = data['password']
            email = data['email']
            library_id = data['library_id']
            store_id = data['store_id']

            try:
                cur = conn.cursor()
                cur.execute(
                    "INSERT INTO users (username, password, email, library_id, store_id) VALUES (%s, %s, %s, %s, %s)", (username, password, email, library_id, store_id))
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

    if 'username' in data and 'password' in data and 'email' in data and library_id in data and store_id in data:
        username = data['username']
        password = data['password']
        email = data['email']
        library_id = data['library_id']
        store_id = data['store_id']

        try:
            cur = conn.cursor()
            cur.execute(
                "UPDATE users SET username = %s, password = %s, email = %s, library_id = %s, store_id =%s WHERE id = %s ", (username, password, email, library_id, store_id, id))
            conn.commit()
            cur.close()

            return jsonify(True)
        except psycopg2.Error as er:
            conn.rollback()
            return abort(400)
    else:
        return abort(400)


@bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM users WHERE id = %s", (id,))
        conn.commit()
        return jsonify(True)

    except:
        conn.rollback()
        return abort(400)
