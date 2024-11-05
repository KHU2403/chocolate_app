from flask import Flask, request, jsonify
from models import Session, FlavorOfTheSeason, Inventory, CustomerFeedback

app = Flask(__name__)
session = Session()

@app.route('/seasonal_flavors', methods=['GET'])
def retrieve_seasonal_flavors():
    flavors = session.query(FlavorOfTheSeason).all()
    result = [{'id': f.id, 'name': f.flavor_name, 'available': f.is_available} for f in flavors]
    return jsonify(result)

@app.route('/seasonal_flavors', methods=['POST'])
def create_seasonal_flavor():
    data = request.get_json()
    flavor = FlavorOfTheSeason(flavor_name=data['name'], is_available=data['available'])
    session.add(flavor)
    session.commit()
    return jsonify({'message': 'New flavor has been added successfully'}), 201

@app.route('/inventory/<int:item_id>', methods=['PUT'])
def update_inventory_item(item_id):
    data = request.get_json()
    item = session.query(Inventory).filter_by(id=item_id).first()
    if item:
        item.stock = data['quantity']
        session.commit()
        return jsonify({'message': 'Stock quantity updated successfully'})
    else:
        return jsonify({'message': 'Inventory item not found'}), 404

@app.route('/feedback', methods=['POST'])
def add_customer_feedback():
    data = request.get_json()
    feedback = CustomerFeedback(
        customer=data['customer_name'],
        suggestion=data['flavor_suggestion'],
        allergy_info=data.get('allergy_concern')
    )
    session.add(feedback)
    session.commit()
    return jsonify({'message': 'Feedback has been recorded'}), 201

if __name__ == '__main__':
    app.run(debug=True)
