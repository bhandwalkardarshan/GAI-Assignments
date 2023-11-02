from flask import Flask, request, jsonify

app = Flask(__name__)

# initializing dictionary
data = {}

# welcome
@app.route('/', methods=['GET'])
def welcome():
    return "Welcome"

# to read all data
@app.route('/items', methods=['GET'])
def get_data():
    return jsonify(data)  

# to create data
@app.route('/item', methods=['POST'])
def create_item():
    item = request.json
    data[item['id']] = item
    return jsonify({'message':'Item Created Successfully!',"item":item})

# to read particular data
@app.route('/items/<int:item_id>', methods=['GET'])
def get_single_item(item_id):
    if item_id in data:
        return jsonify({'message':'Here is your Item',"item":data[item_id]})
    return "Item not found", 404

# to update particular data
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = request.json
    if item_id in data:
        data[item_id] = item
        return jsonify({'message':'Item Updated'})
    return "Item not found", 404

# to delete particular data
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = request.json
    if item_id in data:
        del data[item_id] 
        return jsonify({'message':'Item Deleted'})
    return "Item not found", 404

if(__name__) == "__main__":
    app.run()