from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

stores = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {
                'name': 'My Item',
                'price': 15.99
            }
        ]
    }
]

@app.route('/')
def home():
    return render_template('index.html')
# POST - used to receive data (from the server perspective)
# GET - used to send data back only

# POST /store data: {name:}


@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'itmes': []
    }
    stores.append(new_store)
    return jsonify(new_store)

# GET /store/<string:name> (<string:name>)


@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message':'Error: No such store!'})

# GET /store


@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})

# POST /store/<string:name>/item


@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'Error: No such store!'})  

# Get a list of items in the requested store.
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
        return jsonify({'message':'Error: No such store!'})


app.run(port=5000)