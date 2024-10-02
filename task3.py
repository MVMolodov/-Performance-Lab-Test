import json
import argparse

def read_json(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def find_value(values, test_id):
    if 'values' in values:
        for value in values['values']:
            if value['id'] == test_id:
                # print(test_id, end = ' ')
                # print(value.get('value'))
                return value.get('value')

def fill_values(tests_structure, values):
    if 'tests' in tests_structure:
        for test in tests_structure['tests']:
            fill_values(test, values)
    if 'values' in tests_structure:
        for value in tests_structure['values']:
            fill_values(value, values)
    test_id = tests_structure.get('id')
    if test_id is not None:
        tests_structure['value'] = find_value(values, test_id)

parser = argparse.ArgumentParser(description='Заполнение файла из другого файла')
parser.add_argument('values_file', type=str)
parser.add_argument('tests_file', type=str)
parser.add_argument('report_file', type=str)
args = parser.parse_args()

values = read_json(args.values_file)
tests = read_json(args.tests_file)
fill_values(tests, values)
with open(args.report_file, 'w') as file:
    json.dump(tests, file, indent=4)


