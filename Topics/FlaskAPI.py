from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory "database"
items = {}

# -------------------------------
# 1. GET → Retrieve data
# -------------------------------
@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    if item_id in items:
        return jsonify(items[item_id])
    return jsonify({"error": "Item not found"}), 404

# -------------------------------
# 2. POST → Create new data
# -------------------------------
@app.route("/items", methods=["POST"])
def create_item():
    data = request.get_json()
    item_id = data.get("id")
    items[item_id] = data
    return jsonify({"message": "Item created successfully", "item": data}), 201

# -------------------------------
# 3. PUT → Update/replace data
# -------------------------------
@app.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    data = request.get_json()
    items[item_id] = data
    return jsonify({"message": "Item updated successfully", "item": data})

# -------------------------------
# 4. PATCH → Partial update
# -------------------------------
@app.route("/items/<int:item_id>", methods=["PATCH"])
def patch_item(item_id):
    if item_id not in items:
        return jsonify({"error": "Item not found"}), 404
    data = request.get_json()
    items[item_id].update(data)
    return jsonify({"message": "Item partially updated", "item": items[item_id]})

# -------------------------------
# 5. DELETE → Remove data
# -------------------------------
@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    if item_id in items:
        del items[item_id]
        return jsonify({"message": "Item deleted successfully"})
    return jsonify({"error": "Item not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)