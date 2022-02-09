import yaml
from pprint import pprint

with open('template_toy.yaml') as f:
    data = yaml.safe_load(f)

pprint(data)
template = "{}, {}, {}, {}"

statements = [template.format(el['id'], el['name'], el['status'], el['status_updated']) for el in data['toys']]
with open("create_toys.sql", 'w') as f:
    for statement in statements:
        f.write(statement + '\n')