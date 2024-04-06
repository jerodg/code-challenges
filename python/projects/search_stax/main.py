# * Search through an embedded dict

config = {"schema": {"types": [{"name": "string", "indexed": False, "docValues": True},
                               {"name": "text_general", "indexed": True, "docValues": False},
                               {"name": "text_f", "indexed": True, "docValues": True}],
                     "fields": [{"name": "text1", "type": "text_general"}, {"name": "text2", "type": "string"},
                                {"name": "address", "type": "text_general"}, {"name": "zipcode", "type": "text_f"}]}}


def find(key, value):
    for k, v in (value.items() if isinstance(value, dict) else enumerate(value) if isinstance(value, list) else []):
        if k == key:
            yield v
        elif isinstance(v, (dict, list)):
            for result in find(value, v):
                yield result


def main():
    # config['schema']['types'][value]
    # x = map(itemgetter(value), config)
    # x = list(o[value] for o in config)
    # print(x)
    ls = []
    #
    # print(config['schema']['types'])
    # x = find('name', config['schema']['types'])
    # print(list(x))

    # for x in config['schema']['types']:
    #     ls.append(x['name'])
    #
    # for x in config['schema']['fields']:
    #     ls.append(x['name'])

    for x in config['schema']['types']:
        ls.append(x['name']) if x['indexed'] is True else ''

    # for x in config['schema']['fields']:
    #     ls.append(x['name']) if x['indexed'] is True else ''

    #     print(k, v)
    #     if type()
    #     if type(v) is list:
    #         for x in v:
    #             ls.append(x[value])
    #
    print(ls, sep='\n')


if __name__ == "__main__":
    main()
