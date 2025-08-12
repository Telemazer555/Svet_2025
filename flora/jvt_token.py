import requests

def get_jvt():

    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'PostmanRuntime/7.44.1',
        'Accept': '*/*',
        'Host': 'orchestrator-rolfid-develop.plf-dev.int.rolfcorp.ru',
    }

    json_data = {
        'username': 'st_pk_asp_mitsu',
        'password': 'Ww12345!',
    }

    response = requests.post('https://orchestrator-rolfid-develop.plf-dev.int.rolfcorp.ru/v3/login',
                             headers=headers,
                             json=json_data,
                             verify=False)

    jvt = response.json()['access_token']
    return jvt

