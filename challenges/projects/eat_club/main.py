# Eat Club Assessment by Jerod Gawne
# Missing Shebang
# Missing Header doc-comment/copyright/license
import db
import requests
from check_token_valid import check_token_valid  # These are poorly named
from make_db_order import make_db_order  # These are poorly named

# Providing this code in pdf form makes it much harder as the indents don't copy/paste
# I had to go through and align everything before I could even begin the task.

# Doc-strings should be in triple double-quotes """ comment goes here """
# This is not a valid Python or JSON data structure; perhaps it should be removed?
'''
  payload : {
    name {
      first,
      last
  },
  token, cart_id, user_id
  }
'''

# This is a valid python data structure
payload = {'name':
               {'first': 'John',
                'last': 'Smith'},
           'token': 'asdl;f8yy34oinasdfp8ioh34ep;nuasf',
           'user_id': 'a123456'}

# This is a valid JSON data structure
"""
{
  "name": {
    "first": "John",
    "last": "Smith"
  },
  "token": "asdl;f8yy34oinasdfp8ioh34ep;nuasf",
  "user_id": "a123456"
}
"""


# missing doc-string and type-hints
# payload shadows name from outer scope
def create_order(payload):
    # 'i' shadows name from outer scope;
    # 'cart_id' does not exist in payload
    # variable assignment is unnecessary
    i = payload['cart_id']
    # 'id' shadows name from outer scope
    # variable assignment is unnecessary
    id = payload['user_id']
    # unused variable assignment; also unnecessary
    first_name = payload['name']['first']
    # unused variable assignment; also unnecessary
    last_name = payload['name']['last']
    user_token = payload['token']
    try:
        # unused variable assignment
        # shadows name from outer scope
        res = check_token_valid(user_token, id)
        # should we be returning something here?
    except:  # This is too broad; It should be specified explicitly
        return

    # you should not be using an unsecured API; use https instead
    # use f-strings in lieu of +
    res = requests.get('http://myapi.com/cart' + i)
    valid_items = []
    # .items() is a function not a property
    # not seeing the JSON conversion to a dict
    for i in res.body.items:
        if i['id']:
            if i['price']:
                if i['name']:
                    # are you sure you want to extend here?
                    valid_items.extend([i])
                else:
                    raise ValueError("Menu item name is mandatory;")
            else:
                raise ValueError("Price is a required field")
        else:
            raise ValueError("Id is a required field")

    # This can be merged w/ the next line
    cursor = db.cursor()
    # use f-strings in lieu of +
    cursor.execute("select * from user where id=" + id)
    res = cursor.fetchall()
    # unresolved reference 'chk_user'; did you forget to define the method?
    # this would overwrite the previous assignment if the method were actually written
    # are you sure this is what you want?
    res = chk_user(res.body)
    if res:
        # unnecessary variable assignment; return make_db_order(valid_items)
        order = make_db_order(valid_items)
        return order


# There is a typo/grammar issue in this comment
# we should allow access to only to users of TYPE='app_user' and not
archived  # This should be a comment


# Missing doc-comment, type hint
def chk_user(user):
    # This can be simplified if no additional code is necessary within the nested conditionals
    if user.type == "ap_user":
        if user.archived == "true":
            raise KeyError("User is not active")
        return True
    return False

# Missing if __name__ == '__main__':
