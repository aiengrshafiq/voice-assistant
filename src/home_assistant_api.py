import requests, os
from dotenv import load_dotenv
load_dotenv('../config/.env')

def ha_call(service, entity_id):
    headers = {"Authorization": f"Bearer {os.getenv('HA_TOKEN')}"}
    url = f"{os.getenv('HA_URL')}/api/services/{service}"
    response = requests.post(url, json={"entity_id": entity_id}, headers=headers)
    return response.status_code
