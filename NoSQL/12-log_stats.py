#!/usr/bin/env python3
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    print(logs.nginx_collection.count() + "logs")
    print("Methods:")
    print("\tmethod GET:")
    print("\tmethod POST:")
    print("\tmethod PUT:")
    print("\tmethod PATCH:")
    print("\tmethod DELETE:")

