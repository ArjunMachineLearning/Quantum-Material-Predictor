import numpy as np
from tensorflow.keras.models import load_model
from scripts.fetch_data_api import fetch_material_data
from scripts.preprocess_data import preprocess_data
from scripts.database import Session, Material

model = load_model('models/model.h5', custom_objects={'custom_loss': custom_loss})

def predict_properties(formula):
    data = fetch_material_data(formula)
    input_vector = preprocess_data(data)
    predictions = model.predict(np.array([input_vector]))
    properties = {
        'density': predictions[0][0],
        'melting_point': predictions[0][1],
        'other_property': predictions[0][2]
    }

    with Session() as session:
        material = Material(
            formula=formula,
            density=properties['density'],
            melting_point=properties['melting_point'],
            other_property=properties['other_property']
        )
        session.add(material)
        session.commit()

    return properties
