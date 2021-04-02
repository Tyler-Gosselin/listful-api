from flask import jsonify, request
from app import app, db
from app.models import User, List
from app.schemas import user_schema, users_schema, list_schema, lists_schema


@app.route('/')
def hello_world():
    return "Hello World!!!!!!!!!!!!!"


@app.route('/create-user', methods=['POST'])
def create_user():
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']
    try:
        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
    except:
        return jsonify({"message": "Username is taken"})
    else:
        return jsonify(user_schema.dump(new_user))


@app.route('/users')
def get_users():
    users = User.query.all()
    return jsonify(users_schema.dump(users))


@app.route("/client/log-in", methods=["POST"])
def login():
    post_data = request.get_json()
    db_user = User.query.filter_by(email=post_data.get("email")).first()
    if db_user is None:
        return "Email NOT found", 404
    password = post_data.get("password")
    valid_password = db_user.check_password(password)
    if valid_password:
        return jsonify({"message": "User Verified", "user_id": db_user.id})
    return "password invalid", 401
  
  
@app.route("/user/new-list", methods=['POST'])
def add_list_to_user():
    user_id = request.json['userId']
    title = request.json['title']
    new_list = List(user_id=user_id, title=title)
    db.session.add(new_list)
    db.session.commit()
    return jsonify(list_schema.dump(new_list))

@app.route("/user/lists", methods=['GET'])
def get_all_users():
    all_lists = List.query.all()
    return jsonify(lists_schema.dump(all_lists))

