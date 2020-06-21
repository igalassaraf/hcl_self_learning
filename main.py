# import pymongo
# import nose
import json

class B(object):
    def __init__(self):
        self.c = 'dsfsdfsdfsdf'
        self.d = 1003

    @classmethod
    def from_json(cls, data):
        return cls(**data)

class A(object):
    def __init__(self):
        self.a = 'abc'
        self.b = 100
        self.c = B()

    @classmethod
    def from_json(cls, data):
        c = list(map(B.from_json, data["c"]))
        return cls(c)

class MyDb:
    def __init__(self, machine_address, db_name, user, password, port):
        self.db_uri = 'mongodb://{1}:{2}@{0}:{3}'.format(machine_address, user, password, port)
        self.db_name = db_name

    def connect(self):
        self.mongo_client = pymongo.MongoClient(self.db_uri)
        self.db = self.mongo_client[self.db_name]

    def insert(self, coll_name, doc):
        coll = self.db[coll_name]
        coll.insert_one(doc)

    def find(self, coll_name, query):
        self.db[coll_name].find_one(query)

    def update(self, coll_name, query):
        pass



def main():
    # connect to self_db database in mongodb
    db_obj = MyDb('ic-vm-025.cisco.com', 
        'igal',
        'service',
        'service',
        5022)

    ret = db_obj.connect()
    ret = db_obj.insert('test1', {'s':'fsdfsdf', 'f': {'s':1, 'dfgd': 'sdfdsd0000'}})
    print ret

if __name__ == "__main__":
    # main()
    a = A()
    print (json.dumps(a, lambda o: o.__dict__, sort_keys=True))
    




# def test_db():
#     db = MyDb('ic-vm-025.cisco.com', 
#         'igal',
#         'service',
#         'service',
#         5022)
#     ret = db_obj.connect()
#     asset ret is not None