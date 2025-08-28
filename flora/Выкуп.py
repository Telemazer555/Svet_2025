import requests
import pprint
import jvt_token
import random_vin
from datetime import datetime
from zoneinfo import ZoneInfo
baseurl ="https://fe-flora-host-dev.flora-dev.int.rolfcorp.ru/crm-host/ipz7tahf815l/asp-buyout/"
jvt = jvt_token.get_jvt()

moscow_time = datetime.now(ZoneInfo("Europe/Moscow"))


def url_buyout():
    planned_start_date = moscow_time
    planned_complete_date = moscow_time
    url = "https://proxy-int-dev2.apim-dev.int.rolfcorp.ru/flora/crm-plus/host-needs/v1/needs"
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'ru,en;q=0.9',
        'Authorization': (f'Bearer {jvt}'),
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': 'https://fe-flora-host-dev.flora-dev.int.rolfcorp.ru',
        'Referer': 'https://fe-flora-host-dev.flora-dev.int.rolfcorp.ru/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 YaBrowser/25.6.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="136", "YaBrowser";v="25.6", "Not.A/Brand";v="99", "Yowser";v="2.5"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'x-api-key': 'H9z2aFfrsXWUjoubN2uGSJAX5qSeUHjD',
    }
    json_data = {
    'complex_client_members': [
        {
            # 'client_uuid': 'c26c9e46-c58f-4bfe-b80d-31444a65e309',
            'client_uuid': 'efe44437-c5c3-4587-a3ed-d3ff44736f23',
            'client_type': '5e3354b1-b4f6-4d20-95b7-8df0d6e2b352',
            'principal_uuid': None,
            'roles': [],
        },
    ],
    'need': {
        'good_type_id': 1,
        'good_subtype_id': 2,
        'operation_id': 2,
        'quantity': 1,
        'details': None,
        'description': None,
        'sale_worksheet': {
            'good_type_id': 1,
            'good_subtype_id': 2,
            'operation_id': 2,
            'work_performers_uuid': 'c4b18ace-6f87-445c-9b60-9e042355b099',
            'dealership_uuid': '664480c9-67e8-375f-f8b2-2d3a0fa4cde3',
        },
    },
    'communications': [
        {
            'initiated_by_client': True,
            'is_archive': False,
            'state': 'plan',
            'communication_method': {
                'uuid': '91d6b4e2-33c7-4d17-a47b-80aec89551cc',
            },
            'dealership': {
                'uuid': '664480c9-67e8-375f-f8b2-2d3a0fa4cde3',
            },
            'participants': [
                {
                    'uuid': 'c26c9e46-c58f-4bfe-b80d-31444a65e309',
                },
            ],
            'planned_start_date': '2025-08-22T19:51:42+03:00',
            'planned_complete_date': '2025-08-22T19:59:59+03:00',


        },
    ],
}
    # Придумать метод который будет подтягивать сегодняшнюю дату
    response = requests.post(url,headers=headers,json=json_data,verify = False)
    r = response.json()
    pprint.pprint(r)
    # uuid = (r["sale_worksheet"]["uuid"])

    # return uuid
    return r

if __name__ == '__main__':
    print(random_vin.get_vin())
    print('RRRRRRRTTTT321138')
    print(f'{baseurl}{url_buyout()}')
    print(url_buyout())
