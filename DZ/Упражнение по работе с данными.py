import json
from datetime import datetime, timedelta
from collections import namedtuple

Operator = namedtuple("Operator", ["name", "email"])
operator = Operator(name="Артём", email="forsworn555@yandex.com")

with open("json.json", "r", encoding="utf-8") as file:
    data = json.load(file)


def assert_data(data):
    assert data.get("data"), "Нет заказов в ответе от сервера"
    return len(data["data"])


def assert_time(data):
    format_str = "%Y-%m-%dT%H:%M:%S.%fZ"

    time_start_1 = data['data'][0]['startedAt']
    time_completedAt_1 = data['data'][0]['completedAt']

    time_start_2 = data['data'][1]['startedAt']
    time_completedAt_2 = data['data'][1]['completedAt']

    time_order1 = datetime.strptime(time_start_2, format_str)
    time_order2 = datetime.strptime(time_completedAt_2, format_str)
    time_order3 = datetime.strptime(time_start_1, format_str)
    time_order4 = datetime.strptime(time_completedAt_1, format_str)

    time_time1 = time_order2 - time_order1

    time_time2 = time_order4 - time_order3

    time_run = time_time1 + time_time2

    assert time_run <= timedelta(hours=6)
    assert time_time1 <= timedelta(hours=6)
    assert time_time2 <= timedelta(hours=6)
    return time_run, time_time1, time_time2


def all_orders(data):
    all_refunded = 0
    all_wait_refund = 0
    all_completed = 0

    for i in data['data']:
        all_completed += i['completed']
        all_wait_refund += i['wait_refund']
        all_refunded += i['refunded']
    return all_refunded, all_completed, all_wait_refund


def all_id(data):
    id_report = []
    for item in data['data']:
        if '_id' in item:
            id_report.append(item['_id'])
    id_report.append('326b23a1-e6ab-4b4a-84a1-a3ecb33afc97')

    return id_report


def check_order_conditions(data):
    all_processed = (data['data'][2]['completed'] + data['data'][2]['wait_refund']
                     + data['data'][2]['refunded']) == data['data'][2]['count']

    half_completed = data['data'][2]['completed'] >= (data['data'][2]['count'] / 2)

    refund_ok = data['data'][2]['refunded'] <= data['data'][2]['completed']

    wait_ok = data['data'][2]['wait_refund'] <= data['data'][2]['refunded']

    return all_processed, half_completed, refund_ok, wait_ok


report = {
    "operator": {
        "name": operator.name,
        "email": operator.email
    },
    "order_ids": all_id(data),
    "services_summary": {
        "completed": all_orders(data)[1],
        "refunded": all_orders(data)[0],
        "wait_refund": all_orders(data)[2]
    },
    "conditions": {check_order_conditions(data)}
}

if __name__ == "__main__":

    print(f" Оператор: {report['operator']['name']} ({report['operator']['email']})")
    print("\n Список id заказов:")
    for oid in report['order_ids']:
        print(f" - {oid}")

    print("\n Статус заказов:")
    for k, v in report['services_summary'].items():
        print(f" - {k}: {v}")
    print("\n ")
    print(f'# Заказы есть в базе, в количестве: {assert_data(data)}')
    print(f"# Время выполнения первого и второго заказа {assert_time(data)[0]}")
    print(f"# Время выполнения первого заказа {assert_time(data)[1]}")
    print(f"# Время выполнения второго заказа {assert_time(data)[2]}")
    print("\n ")
    print(f'# Выполнено не меньше половины {check_order_conditions(data)[1]}"')
    print(f'# Возвращено не больше, чем выполнено {check_order_conditions(data)[2]}"')
    print(f'# Ожидающих не больше, чем возвращено {check_order_conditions(data)[3]}"')
