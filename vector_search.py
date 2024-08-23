import requests
import yaml

with open('config/config.yaml') as file:
    config = yaml.safe_load(file)

def search_similar_materials(properties):
    response = requests.post(config['vector_db_url'], json={'vector': properties.tolist()})
    return response.json()
