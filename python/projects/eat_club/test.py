import requests
from check_token_valid import check_token_valid

'''
payload : {
name {
first,
last
},
token, cart_id, user_id
}
'''


def create_order(payload):
    i = payload['cart_id']


id = payload['user_id']
first_name = payload['name']['first']
last_name = payload['name']['last']
user_token = payload['token']
try:
    res = check_token_valid(user_token, id)
except:
    return
res = requests.get('http://myapi.com/cart' + i)
valid_items = []
for i in res.body.items:
    if i['id']:
        if i['price']:
        if i['name']:
        valid_items.extend([i])
else:
    raise ValueError("Menu item name is mandatory;") else:
raise ValueError("Price is a required field") else:
raise ValueError("Id is a required field")
cursor = db.cursor()
cursor.execute("select * from user where id=" + id)
res = cursor.fetchall()
res = chk_user(res.body)
if res:
    order = make_db_order(valid_items)
return order
# we should allow access to only to users of TYPE='app_user' and not
archived


def chk_user(user):
    if user.type == "ap_user":
        if user.archived == "true":
        raise KeyError("User is not active")


return True
return False
