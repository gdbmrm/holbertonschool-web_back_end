#!/usr/bin/env python3
"""
Write a Python function that lists all documents in a collection:
Prototype: def list_all(mongo_collection):
Return an empty list if no document in the collection
mongo_collection will be the pymongo collection object
"""

def list_all(mongo_collection):
    """
    function list_all
    """
    all_doc = []
    docs = mongo_collection.find()

    for doc in docs:
        all_doc.append(doc)

    return all_doc
