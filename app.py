from flask import Flask, request, jsonify, render_template
from models.predict import predict_properties
from scripts.vector_search import search_similar_materials
from scripts.physics_engine import validate_physical_laws
from scripts.database import Session, Material

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    formula = request.form['formula']
    properties = predict_properties(formula)
    
    with Session() as session:
        stored_material = session.query(Material).filter_by(formula=formula).first()
    
    if not validate_physical_laws(properties):
        return jsonify({'error': 'Prediction does not adhere to physical laws'}), 400
    
    similar_materials = search_similar_materials(properties)
    return jsonify({
        'properties': properties,
        'stored_material': {
            'density': stored_material.density if stored_material else None,
            'melting_point': stored_material.melting_point if stored_material else None,
            'other_property': stored_material.other_property if stored_material else None
        },
        'similar_materials': similar_materials
    })

if __name__ == '__main__':
    app.run(debug=True)
