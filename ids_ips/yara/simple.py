
import pathlib
import yara
from pprint import pprint

base_dir = pathlib.Path(__file__).parent.absolute()


rule_path = base_dir.joinpath('rules', 'test.yar').as_posix()

rules = yara.compile(filepath=rule_path)

with open(base_dir.joinpath('sample.txt'), 'rb') as f:
  matches = rules.match(data=f.read())

pprint(matches)

# Output:
#
# {'main': [{'matches': True,
#            'meta': {},
#            'rule': 'test',
#            'strings': [{'data': 'Lorem',
#                         'flags': 19,
#                         'identifier': '$identifier',
#                         'offset': 561},
#                        {'data': 'Lorem',
#                         'flags': 19,
#                         'identifier': '$identifier',
#                         'offset': 2337}],
#            'tags': []}]}