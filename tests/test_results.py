flat_file1 = f'{"{"}\n  - follow: false\n    host: hexlet.io\n' \
             f'  - proxy: 123.234.53.22\n  - timeout: 50\n' \
             f'  + timeout: 20\n  + verbose: true\n{"}"}'

flat_file2 = f'{"{"}\n  - createdAt: 2023-01-16 17:25:00.512426\n' \
             f'  + crush: Neo\n    goodness: true\n  - id: 199\n' \
             f'  + id: 200\n  - job: Leader\n  + job: SubLeader\n' \
             f'  - name: Morpheus\n  + name: Trinity\n{"}"}'

nested_file1 = f'{"{"}\n    common: {"{"}\n      + follow: false\n' \
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
