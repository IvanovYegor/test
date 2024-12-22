# TODO решите задачу
import json


def task() -> float:
    json_file_path = 'input.json'
    with open(json_file_path) as f:
        data = json.load(f)

    total_sum = sum([item['score'] * item['weight'] for item in data])
    return round(total_sum, 3)


print(task())
