# import requests
# import mysql.connector
# import pandas as pd

print('Hello')

# data = requests.get('http://127.0.0.1:8081/products')

data = [
        {
                "id":           1,
                "name":         "ProductName",
                "updated_at":   150000000,
                "price":        100,
                "manufacturer": "ManufacturerCompanyName"
        },
        {
                "id":         3,
                "name":       "ProductName 2",
                "updated_at": 150000230,
                "price":      90
        }
]

data = [
        {"id": 1, "updated_at": 1565641075, "price": 110, "manufacturer": "m2", "name": "Product1"},
        {"id": 2, "updated_at": 1565645377, "price": 100, "name": "Product2"}
]

for row in data:
    mfg = row.get('manufacturer', None)
    m = f'and manufacturer {mfg}' if mfg else 'and no manufacturer'

    print(f'Product {row["name"]} has price {row["price"]} {m}')



import mysql.connector
import pandas as pd
import requests

data = requests.get('http://127.0.0.1:8081/products').json()

for row in data:
    mfg = row.get('manufacturer', None)
    m = f'and manufacturer {mfg}' if mfg else 'and no manufacturer'

    print(f'Product {row["name"]} has price {row["price"]} {m}')
