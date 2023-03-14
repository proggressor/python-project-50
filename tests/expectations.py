flat_stylish1 = f'{"{"}\n  - follow: false\n    host: hexlet.io\n' \
             f'  - proxy: 123.234.53.22\n  - timeout: 50\n' \
             f'  + timeout: 20\n  + verbose: true\n{"}"}'

flat_stylish2 = f'{"{"}\n  - createdAt: 2023-01-16 17:25:00.512426\n' \
             f'  + crush: Neo\n    goodness: true\n  - id: 199\n' \
             f'  + id: 200\n  - job: Leader\n  + job: SubLeader\n' \
             f'  - name: Morpheus\n  + name: Trinity\n{"}"}'

nested_stylish1 = f'{"{"}\n    common: {"{"}\n      + follow: false\n' \
               f'        setting1: Value 1\n      - setting2: 200\n' \
               f'      - setting3: true\n      + setting3: null\n' \
               f'      + setting4: blah blah\n      + setting5: {"{"}\n' \
               f'            key5: value5\n        {"}"}\n        ' \
               f'setting6: {"{"}\n            doge: {"{"}\n              ' \
               f'- wow: \n              + wow: so much\n            {"}"}\n' \
               f'            key: value\n          + ops: vops\n        ' \
               f'{"}"}\n    {"}"}\n    group1: {"{"}\n      - baz: bas\n' \
               f'      + baz: bars\n        foo: bar\n      - nest: {"{"}\n' \
               f'            key: value\n        {"}"}\n      + nest: str\n' \
               f'    {"}"}\n  - group2: {"{"}\n        abc: 12345\n        ' \
               f'deep: {"{"}\n            id: 45\n        {"}"}\n    {"}"}\n' \
               f'  + group3: {"{"}\n        deep: {"{"}\n            id: ' \
               f'{"{"}\n                number: 45\n            {"}"}\n    ' \
               f'    {"}"}\n        fee: 100500\n    {"}"}\n{"}"}'

nested_stylish2 = f"{'{'}\n    Aidan Gillen: {'{'}\n      - aboolean: TRUE\n" \
                  f"      + aboolean: true\n        array: {'{'}\n          " \
                  f"- Game of Thron\"es: The Wire\n          " \
                  f"+ Game of Thrones: The Wire\n        {'}'}\n      " \
                  f"- boolean: true\n      + boolean: false\n      " \
                  f"- int: 2\n      + int: 2\n        object: {'{'}\n       " \
                  f"     foo: bar\n          - object1: {'{'}\n             " \
                  f"   new prop1: new prop value\n            {'}'}\n       " \
                  f"   - object2: {'{'}\n                " \
                  f"new prop1: new prop value\n            {'}'}\n          " \
                  f"- object3: {'{'}\n                " \
                  f"new prop1: new prop value\n            {'}'}\n          " \
                  f"- object4: {'{'}\n                " \
                  f"new prop1: new prop value\n            {'}'}\n        " \
                  f"{'}'}\n      + otherint: 4\n        string: some string" \
                  f"\n    {'}'}\n  + Alexander Skarsg?rd: Generation Kill\n" \
                  f"  - Alexander Skarsgard: Generation Kill\n  " \
                  f"+ Alice Farmer: ['The Corner', 'Oz', 'The Wire']\n  " \
                  f"- Amy Ryan: {'{'}\n        one: In Treatment\n        " \
                  f"two: The Wire\n    {'}'}\n  " \
                  f"+ Amy Ryan: ['In Treatment', 'The Wire']\n    " \
                  f"Annie Fitzgerald: {'{'}\n        Big Love: null\n      " \
                  f"- Oz: Great and Terrible\n      + Oz: Wizzard\n      " \
                  f"+ The Sopranos: 440Hz\n        True Blood: AB\n    " \
                  f"{'}'}\n    Anwan Glover: {'{'}\n        Treme: True\n" \
                  f"        The Wire: False\n    {'}'}\n  " \
                  f"- Clarke Peters: null\n{'}'}"

flat_plain1 = "Property 'follow' was removed\n" \
              "Property 'proxy' was removed\n" \
              "Property 'timeout' was updated. From 50 to 20\n" \
              "Property 'verbose' was added with value: true"

flat_plain2 = "Property 'createdAt' was removed\n" \
              "Property 'crush' was added with value: 'Neo'\n" \
              "Property 'id' was updated. From 199 to 200\n" \
              "Property 'job' was updated. From 'Leader' to 'SubLeader'\n" \
              "Property 'name' was updated. From 'Morpheus' to 'Trinity'"

nested_plain1 = "Property 'common.follow' was added with value: false\n" \
                "Property 'common.setting2' was removed\n" \
                "Property 'common.setting3' was updated. " \
                "From true to null\n" \
                "Property 'common.setting4' was added with value: " \
                "'blah blah'\n" \
                "Property 'common.setting5' was added with value: " \
                "[complex value]\n" \
                "Property 'common.setting6.doge.wow' was updated. " \
                "From '' to 'so much'\n" \
                "Property 'common.setting6.ops' was added with value: " \
                "'vops'\n" \
                "Property 'group1.baz' was updated. From 'bas' to 'bars'\n" \
                "Property 'group1.nest' was updated. " \
                "From [complex value] to 'str'\n" \
                "Property 'group2' was removed\n" \
                "Property 'group3' was added with value: [complex value]"

nested_plain2 = "Property 'Aidan Gillen.aboolean' was updated. " \
                "From 'TRUE' to true\n" \
                "Property 'Aidan Gillen.array.Game of Thron\"es' " \
                "was removed\n" \
                "Property 'Aidan Gillen.array.Game of Thrones' " \
                "was added with value: 'The Wire'\n" \
                "Property 'Aidan Gillen.boolean' was updated. " \
                "From true to false\n" \
                "Property 'Aidan Gillen.int' was updated. From 2 to '2'\n" \
                "Property 'Aidan Gillen.object.object1' was removed\n" \
                "Property 'Aidan Gillen.object.object2' was removed\n" \
                "Property 'Aidan Gillen.object.object3' was removed\n" \
                "Property 'Aidan Gillen.object.object4' was removed\n" \
                "Property 'Aidan Gillen.otherint' was added with value: 4\n" \
                "Property 'Alexander Skarsg?rd' " \
                "was added with value: 'Generation Kill'\n" \
                "Property 'Alexander Skarsgard' was removed\n" \
                "Property 'Alice Farmer' " \
                "was added with value: [complex value]\n" \
                "Property 'Amy Ryan' was updated. " \
                "From [complex value] to [complex value]\n" \
                "Property 'Annie Fitzgerald.Oz' was updated. " \
                "From 'Great and Terrible' to 'Wizzard'\n" \
                "Property 'Annie Fitzgerald.The Sopranos' " \
                "was added with value: '440Hz'\n" \
                "Property 'Clarke Peters' was removed"

flat_json1 = f'{"{"}\n    "follow": {"{"}\n        "value": "false",\n' \
             f'        "category": "deleted"\n    {"}"},\n    ' \
             f'"host": {"{"}\n        "value": "hexlet.io",\n        ' \
             f'"category": "unchanged"\n    {"}"},\n    "proxy": {"{"}\n' \
             f'        "value": "123.234.53.22",\n        ' \
             f'"category": "deleted"\n    {"}"},\n    "timeout": {"{"}\n' \
             f'        "value": [\n            50,\n            20\n        ' \
             f'],\n        "category": "changed"\n    {"}"},\n    ' \
             f'"verbose": {"{"}\n        "value": "true",\n        ' \
             f'"category": "added"\n    {"}"}\n{"}"}'

flat_json2 = f'{"{"}\n    "createdAt": {"{"}\n        ' \
             f'"value": "2023-01-16 17:25:00.512426",\n        ' \
             f'"category": "deleted"\n    {"}"},\n    "crush": {"{"}\n' \
             f'        "value": "Neo",\n        "category": "added"\n    ' \
             f'{"}"},\n    "goodness": {"{"}\n        "value": "true",\n' \
             f'        "category": "unchanged"\n    {"}"},\n    ' \
             f'"id": {"{"}\n        "value": [\n            199,\n' \
             f'            200\n        ],\n        "category": "changed"\n' \
             f'    {"}"},\n    "job": {"{"}\n        "value": [\n' \
             f'            "Leader",\n            "SubLeader"\n        ],\n' \
             f'        "category": "changed"\n    {"}"},\n    ' \
             f'"name": {"{"}\n        "value": [\n            "Morpheus",\n' \
             f'            "Trinity"\n        ],\n        ' \
             f'"category": "changed"\n    {"}"}\n{"}"}'
