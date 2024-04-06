from itertools import groupby

employees = [{'name': 'Kevin Pozzi', 'supervisor': None}, {'name': 'Taylor Jamison', 'supervisor': 'Kevin Pozzi'},
             {'name': 'Katie Viola', 'supervisor': 'Kevin Pozzi'}, {'name': 'Raegan Barker', 'supervisor': 'Taylor Jamison'},
             {'name': 'Casey Corver', 'supervisor': 'Katie Viola'}, ]

sup = lambda x: x['supervisor']
sups = set()

for key, group in groupby(employees, sup):
    sups.add(key)

for s in sups:
    if s is None:
        continue
    else:
        print(s)
        emps = [x['name'] for x in employees if x['supervisor'] == s]
        for e in emps:
            print(f'  --> {e}')
