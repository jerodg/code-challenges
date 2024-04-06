candles = [{"t": "2021-07-14T19:31:00Z", "o": 149.38, "h": 149.43, "l": 149.3701, "c": 149.4, "v": 208144},
           {"t": "2021-07-14T19:32:00Z", "o": 149.3989, "h": 149.515, "l": 149.38, "c": 149.48, "v": 275018},
           {"t": "2021-07-14T19:33:00Z", "o": 149.48, "h": 149.52, "l": 149.409, "c": 149.409, "v": 251242},
           {"t": "2021-07-14T19:34:00Z", "o": 149.405, "h": 149.54, "l": 149.4, "c": 149.51, "v": 307084},
           {"t": "2021-07-14T19:35:00Z", "o": 149.505, "h": 149.56, "l": 149.4701, "c": 149.535, "v": 377666},
           {"t": "2021-07-14T19:36:00Z", "o": 149.54, "h": 149.55, "l": 149.48, "c": 149.5408, "v": 243388},
           {"t": "2021-07-14T19:37:00Z", "o": 149.5432, "h": 149.57, "l": 149.51, "c": 149.535, "v": 212615},
           {"t": "2021-07-14T19:38:00Z", "o": 149.5362, "h": 149.55, "l": 149.5001, "c": 149.515, "v": 193795},
           {"t": "2021-07-14T19:39:00Z", "o": 149.51, "h": 149.52, "l": 149.42, "c": 149.5199, "v": 284613},
           {"t": "2021-07-14T19:40:00Z", "o": 149.515, "h": 149.53, "l": 149.485, "c": 149.5145, "v": 276547},
           {"t": "2021-07-14T19:41:00Z", "o": 149.515, "h": 149.53, "l": 149.4, "c": 149.4, "v": 250545},
           {"t": "2021-07-14T19:42:00Z", "o": 149.405, "h": 149.41, "l": 149.29, "c": 149.3101, "v": 254976},
           {"t": "2021-07-14T19:43:00Z", "o": 149.32, "h": 149.5, "l": 149.19, "c": 149.2, "v": 416948},
           {"t": "2021-07-14T19:44:00Z", "o": 149.1906, "h": 149.2114, "l": 149.17, "c": 149.17, "v": 320980},
           {"t": "2021-07-14T19:45:00Z", "o": 149.175, "h": 149.47, "l": 149.175, "c": 149.4, "v": 429653}, ]


# Example of one entity in the list
# [

#    {
#      "t": 2021-07-14T19:31:00Z, # datetime object str rep, one minute at the finest
#      "o": 172.26, # opening value
#      "h": 172.3,  # highest price of the window
#      "l": 172.16, # the lowest price of the window
#      "c": 172.18,  # closing value
#      "v": 3892, # how many trades happened inside of the window
#    }
# ]


# output
# [
#    {
#      "t": 2021-07-14T19:31:00Z, # datetime object str rep, one minute at the finest
#      "o": 149.38, # opening value
#      "h": max(all h keys),  # highest price of the window
#      "l": min(all l keys), # the lowest price of the window
#      "c": 149.4,  # closing value
#      "v": sum(all v keys), # how many trades happened inside of the window
#    }
# ]


# the api docs from alpaca
# https://alpaca.markets/docs/api-documentation/api-v2/market-data/alpaca-data-api-v1/bars/

# create a function that generates n minute candles from these one minute candles. n can be any integer larger than 1. It's okay
# to generate incomplete intervals


def any_minute_candles(candles, interval):
    res = []
    while candles:
        c = [x for x in candles[:interval]]
        del candles[:interval]
        mino = min(c, key=lambda x: x['l'])
        maxo = max(c, key=lambda x: x['h'])
        vol = sum([x['v'] for x in c])

        try:
            res.append({'t': c[0]['t'], 'o': c[0]['o'], 'h': maxo['h'], 'l': mino['l'], 'c': c[-1]['c'], 'v': vol})
        except IndexError:
            break

    return res


print(*any_minute_candles(candles, 1), sep='\n')
