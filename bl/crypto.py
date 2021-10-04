import time
import datetime


def InsertHistory(mongo, name, amt, rate):

    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    result = mongo.db.crypto.insert_one(
        {'CryptoName': name, 'Amount': amt, 'Rate': rate, 'TimeStamp': st})

    return result.inserted_id
