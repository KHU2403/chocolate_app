from flask import Flask, request, jsonify
from models import Session, SeasonalFlavor, IngredientInventory, CustomerSuggestions

app = Flask(__name__)
session = Session()

@app.route('/flavors', methods=['GET'])
def get_flavors():
    flavors = session.query(SeasonalFlavor).all()
    flavor_list = [{'id': flavor.id, 'flavor_name': flavor.flavor_name, 'is_available': flavor.is_available} for flavor in flavors]
    return jsonify(flavor_list)

@app.route('/flavors', methods=['POST'])
def add_flavor():
    data = request.get_json()
    new_flavor = SeasonalFlavor(flavor_name=data['flavor_name'], is_available=data['is_available'])
    session.add(new_flavor)
    session.commit()
    return jsonify({'message': 'Flavor added successfully'}), 201

@app.route('/ingredients/<int:id>', methods=['PUT'])
def update_ingredient(id):
    data = request.get_json()
    ingredient = session.query(IngredientInventory).filter_by(id=id).first()
    if ingredient:
        ingredient.stock_quantity = data['stock_quantity']
        session.commit()
        return jsonify({'message': 'Ingredient updated successfully'})
    else:
        return jsonify({'message': 'Ingredient not found'}), 404

@app.route('/suggestions', methods=['POST'])
def add_suggestion():
    data = request.get_json()
    new_suggestion = CustomerSuggestions(
        customer_name=data['customer_name'],
        flavor_suggestion=data['flavor_suggestion'],
        allergy_concern=data.get('allergy_concern')
    )
    session.add(new_suggestion)
    session.commit()
    return jsonify({'message': 'Suggestion added successfully'}), 201

if __name__ == '__main__':
    app.run(debug=True)
