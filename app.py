from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data store
users = {}

# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

# GET a specific user
@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({'error': 'User not found'}), 404

# POST - Add a new user
@app.route('/users', methods=['POST'])
def add_user():
    data = request.json
    user_id = data.get('id')
    if user_id in users:
        return jsonify({'error': 'User already exists'}), 400
    users[user_id] = data
    return jsonify({'message': 'User added'}), 201

# PUT - Update a user
@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    if user_id in users:
        users[user_id].update(data)
        return jsonify({'message': 'User updated'}), 200
    return jsonify({'error': 'User not found'}), 404

# DELETE - Remove a user
@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return jsonify({'message': 'User deleted'}), 200
    return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)