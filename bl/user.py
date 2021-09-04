from bson.json_util import dumps
import base64


def Authenticate(mongo,username,password):
    encodepassword = str(base64.b64encode(password.encode("utf-8")))
    print(encodepassword)
    users = mongo.db.user.find({'UserName': username,'PassWord': encodepassword})
    list_users = list(users)
    json_data = dumps(list_users, indent=2, sort_keys=True)
    print(json_data)
    return json_data