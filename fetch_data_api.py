import requests
import yaml

with open('config/config.yaml') as file:
    config = yaml.safe_load(file)

def fetch_material_data(formula):
    response = requests.get(f"{config['oqmd_api_url']}/materials/{formula}")
    return response.json()
