from flask import Flask,render_template,request,jsonify


app = Flask(__name__)

items = [
    {"id":1,"name":"Item 1","description":"This is item 1"},
    {"id":2,"name":"Item 2","description":"This is item 2"}
]

@app.route("/")
def home():
    return "This is my to do list"

# retrieve all the elements of the items
@app.route("/items",methods = ['GET'])
def get_items():
    return jsonify(items)

#retrieve particular element in the items
@app.route("/items/<int:item_id>",methods = ['GET'])
def get_proper_item(item_id):
    item = next((item for item in items if item["id"]==item_id),None)
    if item == None:
        return "jsonify error: element not found"
    else:
        return jsonify(item)

# adding a new element in the items
@app.route("/items",methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return "jsonify error: element not found"
    new_item = {
        "id":items[-1]["id"]+1 if items else 1,
        "name":request.json['name'],
        "description":request.json['description']
    }
    items.append(new_item)
    return jsonify(new_item)


#updating an item in the items
@app.route("/items/<int:item_id>",methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item["id"]==item_id),None)
    if item == None:
        return "element not found"
    items['name'] = request.json.get("name",items["name"])
    items["description"] = request.json.get("description",items["description"])
    return jsonify(item)


# deleting an element in the items
@app.route("/items/<int:item_id>",methods = ["DELETE"])
def delete_item(item_id):
    global items
    items = [item for item in items if item["id"] != item_id]
    return jsonify({"result":"Item deletes"})



if __name__=="__main__":
    app.run(debug = True)