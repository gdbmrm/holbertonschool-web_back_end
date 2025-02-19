#!/usr/bin/env python3
"""
Write a Python function that changes all topics of a school document based on the name:
Prototype: def update_topics(mongo_collection, name, topics):
mongo_collection will be the pymongo collection object
name (string) will be the school name to update
topics (list of strings) will be the list of topics approached in the school
"""

def update_topics(mongo_collection, name, topics):
    """
    function update_topics
    """
    myquery = {"name": name}
    newvalues = { "$set": { "topics": topics }}
    return mongo_collection.update_many(myquery, newvalues)
